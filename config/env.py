from os import getenv
from dotenv import load_dotenv

load_dotenv()

ENV = getenv("ENV")
TOKEN = getenv("TOKEN")
ITAD_TOKEN = getenv("ITAD_TOKEN")


prefix = ""
if ENV == "production":
    prefix = "?"
elif ENV == "development":
    prefix = "."
