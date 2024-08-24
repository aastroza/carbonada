from openai import OpenAI
from loguru import logger
from dotenv import load_dotenv
from carbon.schemas import IndustryQuery, RawQuery
from carbon.resources import PRICING

load_dotenv()

def calculate_cost(model: str, prompt_tokens: int, completion_tokens: int) -> float:
    prices = PRICING[model]
    return prompt_tokens*prices['input']/1000 + completion_tokens*prices['output']/1000

def get_industry(product: str, country: str, model: str) -> (IndustryQuery, float):
    client = OpenAI()
    try:
        completion = client.beta.chat.completions.parse(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": f"You are a helpful carbon footprint calculator. You help users estimate the carbon footprint of their products and services. You can provide information about the carbon footprint of different industries and estimate costs for different products and services. The user lives in {country}.",
                },
                {
                    "role": "user",
                    "content": product,
                },
            ],
            temperature=0.0,
            response_format=IndustryQuery,
        )

        message = completion.choices[0].message
        if message.parsed:
            return message.parsed, calculate_cost(completion.model, completion.usage.prompt_tokens, completion.usage.completion_tokens)
        else:
            logger.error(f"No parsed response was returned. Refusal message: {message.refusal}")
            return None, 0
        
    except Exception as e:
        logger.error(f"An error occurred while querying the OpenAI API: {e}")
        return None, 0

def estimate_raw(product: str, country: str, model: str) -> (RawQuery, float):
    client = OpenAI()
    try:
        completion = client.beta.chat.completions.parse(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": f"You are a helpful carbon footprint calculator. You help users estimate the carbon footprint of their products and services. The user lives in {country}.",
                },
                {
                    "role": "user",
                    "content": product,
                },
            ],
            temperature=0.0,
            response_format=RawQuery,
        )

        message = completion.choices[0].message
        if message.parsed:
            return message.parsed, calculate_cost(completion.model, completion.usage.prompt_tokens, completion.usage.completion_tokens)
        else:
            logger.error(f"No parsed response was returned. Refusal message: {message.refusal}")
            return None, 0
        
    except Exception as e:
        logger.error(f"An error occurred while querying the OpenAI API: {e}")
        return None, 0