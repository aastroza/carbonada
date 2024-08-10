from carbon.schemas import ProductDatasetEntry
import pandas as pd
from pydantic import ValidationError
from loguru import logger

def build_table(df: pd.DataFrame, source: str) -> pd.DataFrame:
    logger.info(f"Building dataset for {source}")
    dataset = []
    for i, row in df.iterrows():
        if source == 'idemat':
            try:
                dataset.append(
                    ProductDatasetEntry(product = row['Process'],
                                        carbon_footprint = row['Carbon'],
                                        source = source)
                )
            except ValidationError as e:
                logger.error(f"Validation error in row {i}: {e}")
        elif source == 'catalogue':
            try:
                dataset.append(
                    ProductDatasetEntry(product = row['Product name (and functional unit)'] + ' - ' + str(row['Product detail']),
                                        carbon_footprint = row["Product's carbon footprint (PCF, kg CO2e)"],
                                        source = source)
                )
            except ValidationError as e:
                logger.error(f"Validation error in row {i}: {e}")
        else:
            logger.error(f"Unknown source: {source}")
    
    return pd.DataFrame([data.model_dump() for data in dataset])