from modal import Image, App

image = Image.debian_slim().pip_install(
    "loguru",
    "pandas",
    "openpyxl",
    "openai==1.40.0",
    "scikit-learn==1.5.1",
    "pyarrow",
    "psycopg2-binary",
    "python-dotenv")

app = App("carbonada")