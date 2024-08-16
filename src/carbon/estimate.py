import pandas as pd
from loguru import logger
from carbon.llm import get_industry
from carbon.schemas import Estimation

df = pd.read_excel('../data/processed/industry.xlsx')
df['industry'] = [s.replace('\xa0', '').strip() for s in df['industry']]

def estimate_carbon_footprint_using_industry(industry: str, cost: float = 10, country: str = 'Chile') -> float:
    df_country = df[df['country'] == country]
    carbon_footprint_per_USD = df_country[df_country['industry'] == industry]['carbon_footprint_per_USD'].values[0]
    return cost*carbon_footprint_per_USD, carbon_footprint_per_USD


def estimate_carbon_footprint(product: str, country: str = 'Chile', model: str = 'gpt-4o-2024-08-06') -> float:
    query = get_industry(product, country, model)
    if query is None:
        return None
    
    carbon_footprint, carbon_footprint_per_USD = estimate_carbon_footprint_using_industry(query.industry.value, query.cost, country)
    
    estimation = Estimation(
                    product=product,
                    industry=query.industry,
                    carbon_footprint=carbon_footprint,
                    carbon_footprint_per_USD=carbon_footprint_per_USD,
                    country=country,
                    cost=query.cost,
                    cost_reasoning=query.cost_reasoning,
                    source="SWC MRIO Dataset",
                    model=model,
    )
    
    return estimation

def estimation_to_string(estimate: Estimation)-> str:
    return f"""The estimated carbon footprint of {estimate.product} in {estimate.country} is {estimate.carbon_footprint:.2f} kg CO2e.
This estimate was calculated using data from {estimate.source}, which provides information about the carbon footprint per USD ({estimate.carbon_footprint_per_USD:.2f}) for the {estimate.industry} industry in {estimate.country}.
The total cost of the product was estimated by {estimate.model}, amounting to {estimate.cost:.2f} USD.
The reasoning behind this estimate is as follows: {estimate.cost_reasoning}"""
