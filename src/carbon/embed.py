from sklearn.metrics.pairwise import cosine_similarity
from typing import List
from openai import OpenAI
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from carbon.schemas import Estimation, Confidence
load_dotenv()

client = OpenAI()


def semantic_similarity_search(query: str, df: pd.DataFrame, model: str = "text-embedding-3-small", treshold: List[float] = [0.9, 0.8], top_k: int = 1):
    doc_embeddings = df['prod_embedding'].tolist()


    docs = df['product (esp)'].tolist()
    sources = df['source'].tolist()
    footprints = df['carbon_footprint'].tolist()
    units = df['Medida'].tolist()
    quantities = df['Cantidad'].tolist()
    # Calcular el embedding del query
    embedding_query = client.embeddings.create(input = [query], model=model).data[0].embedding
    # Calcular la similitud de coseno entre los embeddings de los textos y los embeddings de los tópicos
    similitudes = cosine_similarity(doc_embeddings, [embedding_query])
    similitudes = [similitudes[i][0] for i in range(len(similitudes))]
    # guardamos el documento con la mayor similaridad
    top_k_indices = np.argsort(similitudes)[-top_k:][::-1]
    top_k_textos = [docs[i] for i in top_k_indices]
    top_k_similitudes = [similitudes[i] for i in top_k_indices]
    top_k_sources = [sources[i] for i in top_k_indices]
    top_k_footprints = [footprints[i] for i in top_k_indices]
    top_k_units = [units[i] for i in top_k_indices]
    top_k_quantities = [quantities[i] for i in top_k_indices]

    if top_k_similitudes[0] >= treshold[0]:
        estimation = Estimation(
                            product=top_k_textos[0],
                            industry="",
                            carbon_footprint=top_k_footprints[0],
                            carbon_footprint_per_USD=0,
                            carbon_footprint_call=0,
                            country="",
                            cost=0,
                            cost_reasoning="",
                            confidence=Confidence.high,
                            similarity=top_k_similitudes[0],
                            source=top_k_sources[0],
                            explanation = f"La huella de carbono estimada de **{top_k_textos[0]}** es de **{top_k_footprints[0]}** kg CO2e. Esta estimación es para **{top_k_quantities[0]} {top_k_units[0]}** según los datos de **{top_k_sources[0]}**.",
                            model=model,
            )
        return estimation
    elif top_k_similitudes[0] >= treshold[1]:
        estimation = Estimation(
                                product=top_k_textos[0],
                                industry="",
                                carbon_footprint=top_k_footprints[0],
                                carbon_footprint_per_USD=0,
                                carbon_footprint_call=0,
                                country="",
                                cost=0,
                                cost_reasoning="",
                                confidence=Confidence.medium,
                                similarity=top_k_similitudes[0],
                                source=top_k_sources[0],
                                explanation = f"La huella de carbono estimada de **{top_k_textos[0]}** es de **{top_k_footprints[0]}** kg CO2e. Esta estimación es para **{top_k_quantities[0]} {top_k_units[0]}** según los datos de **{top_k_sources[0]}**.",
                                model=model,
                )
        return estimation
    else:
        return None