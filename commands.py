import requests
from os import getenv
from dotenv import load_dotenv
import nextcord

from core.utils import convert_date
from models.game import Game

load_dotenv()

API_KEY = getenv("API_KEY")
BASE_URL = getenv("BASE_URL")


def gsearch_command(query: str):
    url_query = f"https://{BASE_URL}/v1/Games/ByGameName"
    developer_query = f"https://{BASE_URL}/v1/Developers/ByDeveloperID"
    thumb_base_url = "https://cdn.thegamesdb.net/images/thumb/"

    base_response = requests.get(
        url_query, params={"apikey": API_KEY, "name": query}
    ).json()

    game = [
        {
            "game_id": base_response["data"]["games"][0]["id"],
            "game_title": base_response["data"]["games"][0]["game_title"],
            "developers": base_response["data"]["games"][0]["developers"],
            "release_date": base_response["data"]["games"][0]["release_date"],
        }
    ]

    dev_id = str(game[0]["developers"][0])
    developer_response = requests.get(
        developer_query, params={"apikey": API_KEY, "id": dev_id}
    ).json()
    dev_name = developer_response["data"]["developers"][dev_id]["name"]

    gameObject = Game(
        title=game[0]["game_title"],
        small_thumb=f"{thumb_base_url}boxart/front/{game[0]['game_id']}-1.jpg",
        developer=dev_name,
        release_date=game[0]["release_date"],
    )

    # Assembles the final embed
    embed = nextcord.Embed(
        title=gameObject.get_title(),
        description=f"Developer: {gameObject.get_developer()}\nRelease Date: {convert_date(gameObject.get_release_date())}",
    )
    embed.set_image(url=gameObject.get_small_thumb())
    embed.set_footer(text="Data provided by TheGamesDB")

    print(f"Title: {gameObject.get_title()}")
    print(f"Small Thumb: {gameObject.get_small_thumb()}")
    print(f"Developer: {gameObject.get_developer()}")
    print(f"Release Date: {convert_date(gameObject.get_release_date())}")
    
    return embed
