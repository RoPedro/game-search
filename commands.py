import requests
from os import getenv
from dotenv import load_dotenv
import nextcord
import json

from core.utils import convert_date
from core.igdb_auth import wrapper
from models.game import Game

load_dotenv()


def gsearch_command(query: str):
    game_response = wrapper.api_request(
        "games",
        f'fields name, involved_companies.company.name, first_release_date, cover.url; search "{query}"; where game_type = 0; limit 4;',
    )
    igdb_data = json.loads(game_response)

    game = [
        {
            "game_id": igdb_data[0]["id"],
            "game_title": igdb_data[0]["name"],
            "developer": igdb_data[0]["involved_companies"][0]["company"]["name"],
            "release_date": igdb_data[0][
                "first_release_date"
            ],  # Unix timestamp, needs conversion
            "small_thumb": igdb_data[0]["cover"]["url"].replace(
                "t_thumb", "t_cover_big"
            ),
        }
    ]

    gameObject = Game(
        title=game[0]["game_title"],
        developer=game[0]["developer"],
        release_date=game[0]["release_date"],
        small_thumb="https:" + game[0]["small_thumb"],
    )

    # Assembles the final embed
    embed = nextcord.Embed(
        title=gameObject.get_title(),
        description=f"Developer: {gameObject.get_developer()}\nRelease Date: {convert_date(gameObject.get_release_date())}",
    )
    embed.set_image(url=gameObject.get_small_thumb())
    embed.set_footer(text="Data provided by IGDB")

    print(f"Title: {gameObject.get_title()}")
    print(f"Small Thumb: {gameObject.get_small_thumb()}")
    print(f"Developer: {gameObject.get_developer()}")
    print(f"Release Date: {convert_date(gameObject.get_release_date())}")

    return embed
