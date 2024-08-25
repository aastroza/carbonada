import pandas as pd
from carbon.llm import get_industry
from carbon.schemas import Estimation, Confidence
from carbon.embed import semantic_similarity_search
from carbon.llm import query_response_relation

df = pd.read_excel('https://github.com/aastroza/carbonada/raw/master/data/processed/industry.xlsx')
df['industry'] = [s.replace('\xa0', '').strip() for s in df['industry']]

df_product= pd.read_parquet('https://github.com/aastroza/carbonada/raw/master/data/processed/product_cleaned.parquet')

def estimate_carbon_footprint_using_industry(industry: str, cost: float = 10, country: str = 'Chile') -> float:
    """
    Estimates the carbon footprint based on industry data for a specific country.

    This function calculates the carbon footprint by multiplying the cost of a product or service 
    by the carbon footprint per USD value associated with a particular industry in a given country.

    :param industry: The industry for which the carbon footprint is being estimated.
    :param cost: The cost of the product or service in USD. Default is 10 USD.
    :param country: The country where the product or service is located. Default is 'Chile'.
    :return: A tuple containing the estimated carbon footprint (in kg CO2e) and the carbon footprint per USD value.
    """
    df_country = df[df['country'] == country]
    carbon_footprint_per_USD = df_country[df_country['industry'] == industry]['carbon_footprint_per_USD'].values[0]
    return cost*carbon_footprint_per_USD, carbon_footprint_per_USD

def estimate_carbon_footprint_using_products(product: str) -> float:
    estimation  = semantic_similarity_search(product, df_product)
    return estimation

def estimate_carbon_footprint(product: str, country: str = 'Chile', model: str = 'gpt-4o-mini-2024-07-18') -> float:
    """
    Estimates the carbon footprint for a specific product in a given country using a specified model.

    This function determines the industry associated with a product and then uses this industry to 
    estimate the carbon footprint based on the cost of the product. The estimation considers the 
    carbon footprint per USD for the industry and country provided.

    :param product: The name of the product for which the carbon footprint is being estimated.
    :param country: The country where the product is located. Default is 'Chile'.
    :param model: The model used to estimate the cost of the product. Default is 'gpt-4o-2024-08-06'.
    :return: An Estimation object containing details of the carbon footprint estimation, 
             or None if the industry could not be determined.
    """
    query = estimate_carbon_footprint_using_products(product)
    if query is not None:
        query_relevance = query_response_relation(product, query.product, model)
    else:
        query_relevance = False
    if query is None or query_relevance is False:
        query, cost = get_industry(product, country, model)
        if query is None:
            return None
        
        carbon_footprint, carbon_footprint_per_USD = estimate_carbon_footprint_using_industry(query.industry.value, query.cost, country)
        carbon_footprint_call, carbon_footprint_per_USD_call = estimate_carbon_footprint_using_industry("Information Service Activities", cost, country)

        explanation = (
            f"Esta estimación se calculó utilizando datos del conjunto **SWC MRIO**, "
            f"que proporciona información sobre la huella de carbono por USD "
            f"({carbon_footprint_per_USD:.2f}) para la industria *{query.industry.value}* en {country}.\n"
            f"El costo total del producto fue estimado por {model}, "
            f"ascendiendo a {query.cost:.2f} USD.\n\n"
            f"El razonamiento detrás de esta estimación es el siguiente: {query.cost_reasoning}\n\n"
        )
        estimation = Estimation(
                        product=product,
                        industry=query.industry,
                        category="otros",
                        carbon_footprint=carbon_footprint,
                        carbon_footprint_per_USD=carbon_footprint_per_USD,
                        carbon_footprint_call=carbon_footprint_call,
                        country=country,
                        cost=query.cost,
                        cost_reasoning=query.cost_reasoning,
                        confidence=Confidence.low,
                        similarity=0,
                        source="SWC MRIO Dataset",
                        explanation=explanation,
                        model=model,
        )
    else:
        estimation = query
    
    return estimation

def estimation_to_string(estimate: Estimation, language: str = 'spanish')-> str:
    """
    Converts an Estimation object into a formatted string that describes the carbon footprint estimation.
    
    :param estimate: Estimation object containing the details of the estimation.
    :return: A formatted string with the estimation details.
    """
    if language == 'spanish':
        return (
            f"La **huella de carbono estimada** de **{estimate.product}** en **{estimate.country}** "
            f"es de **{estimate.carbon_footprint:.2f} kg CO2e**.\n\n"
            f"Esta estimación se calculó utilizando datos de **{estimate.source}**, "
            f"que proporciona información sobre la huella de carbono por USD "
            f"({estimate.carbon_footprint_per_USD:.2f}) para la industria *{estimate.industry}* en {estimate.country}.\n"
            f"El costo total del producto fue estimado por {estimate.model}, "
            f"ascendiendo a {estimate.cost:.2f} USD.\n\n"
            f"El razonamiento detrás de esta estimación es el siguiente: {estimate.cost_reasoning}\n\n"
            f"La huella de carbono estimada de esta consulta a la API es {estimate.carbon_footprint_call*1000:.3f} g CO2e."
        )
    else:
        return (
            f"The **estimated carbon footprint** of **{estimate.product}** in **{estimate.country}** "
            f"is **{estimate.carbon_footprint:.2f} kg CO2e**.\n\n"
            f"This estimate was calculated using data from **{estimate.source}**, "
            f"which provides information about the carbon footprint per USD "
            f"({estimate.carbon_footprint_per_USD:.2f}) for the *{estimate.industry}* industry in {estimate.country}.\n"
            f"The total cost of the product was estimated by {estimate.model}, "
            f"amounting to {estimate.cost:.2f} USD.\n\n"
            f"The reasoning behind this estimate is as follows: {estimate.cost_reasoning}\n\n"
            f"The estimated carbon footprint of this api query is {estimate.carbon_footprint_call*1000:.3f} g CO2e."
        )
