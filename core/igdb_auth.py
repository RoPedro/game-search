from igdb.wrapper import IGDBWrapper
from dotenv import load_dotenv
from os import getenv

load_dotenv()

IGDB_CLIENT_ID = getenv("IGDB_CLIENT_ID")
IGDB_TOKEN = getenv("IGDB_TOKEN")

wrapper = IGDBWrapper(str(IGDB_CLIENT_ID), str(IGDB_TOKEN))
