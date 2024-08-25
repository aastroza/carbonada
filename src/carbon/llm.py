from openai import OpenAI
from loguru import logger
from dotenv import load_dotenv
from carbon.schemas import IndustryQuery, RawQuery
from carbon.resources import PRICING

load_dotenv()

client = OpenAI()

def translate_to_english(text: str) -> str:
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
            "role": "system",
            "content": "You will be provided with a sentence, and your task is to translate it into English."
            },
            {
            "role": "user",
            "content": text,
            }
        ],
    )
    response = completion.choices[0].message.content
    return response

def check_moderation(query: str) -> bool:
    translated_query = translate_to_english(query)
    response = client.moderations.create(input=f"{translated_query}, but translated to English")
    response_dict = response.model_dump()
    logger.info(f"Moderation response: {response_dict}")
    is_flagged = response_dict['results'][0]['flagged']
    return is_flagged

def calculate_cost(model: str, prompt_tokens: int, completion_tokens: int) -> float:
    prices = PRICING[model]
    return prompt_tokens*prices['input']/1000 + completion_tokens*prices['output']/1000

def get_industry(product: str, country: str, model: str) -> (IndustryQuery, float):
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

def query_response_relation(query: str, response: str, model: str = "gpt-4o-mini") -> bool:
    completion = client.chat.completions.create(
    model=model,
    messages = [
        {"role": "system", "content": "You are a helpful assistant that determines if two products or services belong to the same thing or if they refer to the same topic."},

        # Few-shot example 1
        {"role": "user", "content": "Query: Un lavado de autos\nResponse: Lavadora\n"},
        {"role": "assistant", "content": "no"},

        {"role": "user", "content": "Query: hamburguesa de queso\nResponse: hamburguesa de carne\n"},
        {"role": "assistant", "content": "yes"},

        # Few-shot example 2
        {"role": "user", "content": "Query: Un electrodoméstico\nResponse: Lavavajillas\n"},
        {"role": "assistant", "content": "yes"},

        # Few-shot example 3
        {"role": "user", "content": "Query: Un viaje en avión de 1 hora\nResponse: Un viaje en tren de 30 minutos\n"},
        {"role": "assistant", "content": "no"},

        # Few-shot example 4
        {"role": "user", "content": "Query: hamburguesa vegana\nResponse: hamburguesa\n"},
        {"role": "assistant", "content": "yes'"},

        # Few-shot example 5
        {"role": "user", "content": "Query: manzana verde\nResponse: manzana\n"},
        {"role": "assistant", "content": "yes"},

        # User's actual prompt
        {"role": "user", "content": f"Query: {query}\nResponse: {response}"}
    ]


    )
    response = completion.choices[0].message.content
    if "yes" in response:
        return True
    else:
        return False