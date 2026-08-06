import logging
from os import getenv
from dotenv import load_dotenv
import json

from src.translations.langs import LANGS
from config.logger import setup_logging

setup_logging()
log = logging.getLogger(__name__)

load_dotenv()

ENV = getenv("ENV")
LANG = getenv("LANG")

DISCORD_BOT_TOKEN = getenv("DISCORD_BOT_TOKEN")
if DISCORD_BOT_TOKEN is None:
    log.error("Discord Bot Token missing, it will be not able to connect to Discord")
ITAD_TOKEN = getenv("ITAD_TOKEN")


if LANG in LANGS:
    with open(f"src/translations/{LANG}.json", "r") as translation_file:
        lang_data = json.load(translation_file)
else:
    if LANG == "":
        log.warning(
            "LANG environment variable is empty, region and language will default English"
        )
    else:
        log.warning(
            "LANG environment variable is invalid, region and language will default to English."
        )
    LANG = "US"
    with open(f"src/translations/{LANG}.json", "r") as translation_file:
        lang_data = json.load(translation_file)


prefix = "?"
if ENV == "development":
    prefix = "."
