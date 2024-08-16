from openai import OpenAI
from carbon.schemas import Query
from loguru import logger

def get_industry(product: str, country: str, model: str) -> Query:
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
            response_format=Query,
        )

        message = completion.choices[0].message
        if message.parsed:
            return message.parsed
        else:
            logger.error(f"No parsed response was returned. Refusal message: {message.refusal}")
            return None
        
    except Exception as e:
        logger.error(f"An error occurred while querying the OpenAI API: {e}")
        return None