from pydantic import BaseModel

class ProductDatasetEntry(BaseModel):
    product: str
    carbon_footprint: float
    source: str

class IndustryDatasetEntry(BaseModel):
    industry: str
    country: str
    carbon_footprint_per_USD: float
    source: str