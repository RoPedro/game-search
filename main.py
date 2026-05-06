import requests
from dotenv import load_dotenv
from os import getenv
import nextcord
from nextcord.ext import commands

from models.game import Game
from core.utils import convert_date


load_dotenv()

API_KEY = getenv("API_KEY")
BASE_URL = getenv("BASE_URL")
TOKEN = getenv("TOKEN")

# Define intents so it can read message content (required for commands to work)
intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="?", intents=intents)


@bot.command(name="gsearch", description="Search for a game by its name")
async def gsearch(ctx, *, query: str):
    url_query = f"https://{BASE_URL}/v1/Games/ByGameName"
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
        f"https://{BASE_URL}/v1/Developers/ByDeveloperID?apikey={API_KEY}&id={dev_id}"
    ).json()
    dev_name = developer_response["data"]["developers"][dev_id]["name"]
    
    gameObject = Game(
        title=game[0]["game_title"],
        small_thumb=f"{thumb_base_url}boxart/front/{game[0]['game_id']}-1.jpg",
        developer=dev_name,
        release_date=game[0]["release_date"],
    )

    embed = nextcord.Embed(
        title=gameObject.get_title(),
        description=f"Developer: {gameObject.get_developer()}\nRelease Date: {convert_date(gameObject.get_release_date())}",
    )
    embed.set_thumbnail(url=gameObject.get_small_thumb())
    embed.set_footer(text="Data provided by TheGamesDB")

    await ctx.send(embed=embed)

    print(f"Title: {gameObject.get_title()}")
    print(f"Small Thumb: {gameObject.get_small_thumb()}")
    print(f"Developer: {gameObject.get_developer()}")
    print(f"Release Date: {convert_date(gameObject.get_release_date())}")


bot.run(str(TOKEN))
