from modal import Secret, web_endpoint
from loguru import logger
from pydantic import BaseModel
from carbon.estimate import estimate_carbon_footprint
from carbon.modal_setup import app, image
from carbon.cache import log_results, cache_results, get_cached_results

class Query(BaseModel):
    product: str

@app.function(image=image, secrets=[Secret.from_dotenv()], keep_warm=1)
@web_endpoint(method="POST")
def estimate(query: Query):

    cached_result = get_cached_results(query.product)
    if cached_result:
        logger.info("Using cached results")
        return cached_result

    logger.info(f"Estimating carbon footprint for product: {query.product}")
    estimation = estimate_carbon_footprint(query.product)
    cache_results(query.product, estimation.dict())
    log_results(query.product, estimation.dict())
    return estimation