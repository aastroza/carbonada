import pandas as pd
from carbon.llm import get_industry
from carbon.schemas import Estimation, Confidence

df = pd.read_excel('https://github.com/aastroza/carbonada/raw/master/data/processed/industry.xlsx')
df['industry'] = [s.replace('\xa0', '').strip() for s in df['industry']]

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
    query, cost = get_industry(product, country, model)
    if query is None:
        return None
    
    carbon_footprint, carbon_footprint_per_USD = estimate_carbon_footprint_using_industry(query.industry.value, query.cost, country)
    carbon_footprint_call, carbon_footprint_per_USD_call = estimate_carbon_footprint_using_industry("Information Service Activities", cost, country)

    estimation = Estimation(
                    product=product,
                    industry=query.industry,
                    carbon_footprint=carbon_footprint,
                    carbon_footprint_per_USD=carbon_footprint_per_USD,
                    carbon_footprint_call=carbon_footprint_call,
                    country=country,
                    cost=query.cost,
                    cost_reasoning=query.cost_reasoning,
                    confidence=Confidence.low,
                    source="SWC MRIO Dataset",
                    model=model,
    )
    
    return estimation

def estimation_to_string(estimate: Estimation)-> str:
    """
    Converts an Estimation object into a formatted string that describes the carbon footprint estimation.
    
    :param estimate: Estimation object containing the details of the estimation.
    :return: A formatted string with the estimation details.
    """
    return (
        f"The estimated carbon footprint of {estimate.product} in {estimate.country} "
        f"is {estimate.carbon_footprint:.2f} kg CO2e.\n"
        f"This estimate was calculated using data from {estimate.source}, "
        f"which provides information about the carbon footprint per USD "
        f"({estimate.carbon_footprint_per_USD:.2f}) for the {estimate.industry} industry in {estimate.country}.\n"
        f"The total cost of the product was estimated by {estimate.model}, "
        f"amounting to {estimate.cost:.2f} USD.\n"
        f"The reasoning behind this estimate is as follows: {estimate.cost_reasoning}"
    )
