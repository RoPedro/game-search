from datetime import datetime
from models.game import Game

"""
DEPRECATION WARNING: under the hood, Nextcord uses `asyncio.iscoroutinefunction(value)` when importing it's
functions, which will be removed in Python 3.16. Before considering updating to 3.16, check for this 
compatibility issue on Nextcord.
"""
from nextcord import Embed, ui
import logging

from integrations.isThereAnyDeal import get_itad_price, ITAD_ICON

log = logging.getLogger(__name__)


# Don't crash if date is invalid
def convert_date(date_stamp):
    if date_stamp is None:
        return "Unknown"
    try:
        return datetime.fromtimestamp(date_stamp).strftime("%d/%m/%Y")
    except ValueError:
        return None


def create_games_array(igdb_data, limit):
    games = []
    for game in range(limit):  # Limit = number of games to show, default is 4.
        try:
            data_developer, data_publisher = find_set_companies(
                igdb_data[game]
            )  # send the index so it knows what game is. (data[game_index])
            external_id = assign_external_id(igdb_data[game])

            game = Game(  # iterate with game because igdb games list don't have a "game" key, so number instead.
                title=igdb_data[game]["name"],
                slug=igdb_data[game]["slug"],
                external_id=external_id,
                developer=data_developer,
                publisher=data_publisher,
                release_date=igdb_data[game]["first_release_date"],
                small_thumb="https:"
                + igdb_data[game]["cover"]["url"].replace("t_thumb", "t_1080p"),
            )
            game.find_dominant_color()
            games.append(game)
        except (IndexError, KeyError) as error:
            log.debug(error)
            continue
    return games


def find_set_companies(igdb_data):
    developer, publisher = "", ""
    for company in igdb_data["involved_companies"]:  # loop in involved companies
        if company["developer"] == True:
            developer = company["company"]["name"]
            if (
                company["publisher"] == True
            ):  # Avoids publisher being empty if developer and publisher is true
                publisher = company["company"]["name"]
        elif company["publisher"] == True:
            publisher = company["company"]["name"]

    return developer, publisher


def assign_external_id(igdb_data):
    external_id = ""
    log.debug(igdb_data["slug"])
    for ex_game in igdb_data["external_games"]:
        if (ex_game["external_game_source"]["name"]) == "Steam":
            external_id = ex_game["uid"]

    return external_id


def build_menu(games):
    from models.menu import GamesDropdown

    menu = ui.View()
    menu.add_item(GamesDropdown(games))
    return menu


def build_embed(games):
    embed = Embed(
        title=games[0].get_title(),
        description=f"Developer: {games[0].get_developer()}\nPublisher: {games[0].get_publisher()}\nRelease Date: {convert_date(games[0].get_release_date())}",
        colour=int(
            games[0].get_dominant_color(), 16
        ),  # Need to specify 16 since we're passing a hexadecimal string
    )
    embed.set_image(url=games[0].get_small_thumb())
    embed.set_footer(text="Data provided by IGDB")

    log.debug(f"Title: {games[0].get_title()}")
    log.debug(f"Small Thumb: {games[0].get_small_thumb()}")
    log.debug(f"Developer: {games[0].get_developer()}")
    log.debug(f"Publisher: {games[0].get_publisher()}")
    log.debug(f"Release Date: {convert_date(games[0].get_release_date())}")

    return embed

async def build_prices_embed(games):
    result = get_itad_price(games[0].get_external_id())
    if result == "":
        return None
    
    current_price = result[0] # 0 = Current Price
    hist_low = result[1] # 1 = Historical Low
    
    prices_embed = Embed(
        title=f"💸 Deals and price for {games[0].get_title()} 💸",
        description=f"Current Price: {current_price["amount"]} ({current_price["cut"]}%)\n"
                    f"Historical Low: {hist_low["amount"]} ({hist_low["cut"]}%)"
    )
    prices_embed.set_footer(text=f"Data provided by isThereAnyDeal", icon_url=ITAD_ICON)
    
    return prices_embed