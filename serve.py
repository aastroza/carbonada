from modal import Secret, web_endpoint
from loguru import logger
from pydantic import BaseModel
from carbon.estimate import estimate_carbon_footprint
from carbon.modal_setup import app, image

class Query(BaseModel):
    product: str

@app.function(image=image, secrets=[Secret.from_dotenv()])
@web_endpoint(method="POST")
def estimate(query: Query):
    logger.info(f"Estimating carbon footprint for product: {query.product}")
    estimation = estimate_carbon_footprint(query.product)
    return estimation