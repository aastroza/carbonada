from modal import Image, App

image = Image.debian_slim().pip_install(
    "loguru",
    "pandas",
    "openpyxl",
    "openai==1.40.0",
    "python-dotenv")

app = App("carbonada")