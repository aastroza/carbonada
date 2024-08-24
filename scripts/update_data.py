from modal import Image, App, Dict
from loguru import logger

image = Image.debian_slim().pip_install(
    "pandas",
    "loguru")

app = App("carbonada-data")

df = Dict.from_name("df-data", create_if_missing=True)