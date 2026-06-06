from datetime import datetime
from models.game import Game

'''
DEPRECATION WARNING: under the hood, Nextcord uses `asyncio.iscoroutinefunction(value)` when importing it's
functions, which will be removed in Python 3.16. Before considering updating to 3.16, check for this 
compatibility issue on Nextcord.
'''
from nextcord import Embed, ui
import logging

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
            
            game = Game(  # iterate with game because igdb games list don't have a "game" key, so number instead.
                title=igdb_data[game]["name"],
                slug=igdb_data[game]["slug"],
                developer=data_developer,
                publisher=data_publisher,
                release_date=igdb_data[game]["first_release_date"],
                small_thumb="https:"
                + igdb_data[game]["cover"]["url"].replace("t_thumb", "t_1080p"),
            )
            game.find_dominant_color()
            games.append(game)
        except (IndexError, KeyError):
            continue
    return games


def find_set_companies(igdb_data):
    developer, publisher = "", ""
    for company in igdb_data["involved_companies"]:  # loop in involved companies
        if company["developer"] == True:
            developer = company["company"]["name"]
        elif company["publisher"] == True:
            publisher = company["company"]["name"]

    return developer, publisher


def build_menu(games):
    from models.menu import GamesDropdown

    menu = ui.View()
    menu.add_item(GamesDropdown(games))
    return menu


def build_embed(games):
    embed = Embed(
        title=games[0].get_title(),
        description=f"Developer: {games[0].get_developer()}\nPublisher: {games[0].get_publisher()}\nRelease Date: {convert_date(games[0].get_release_date())}",
        colour=int(games[0].get_dominant_color(), 16), # Need to specify 16 since we're passing a hexadecimal string
    )
    embed.set_image(url=games[0].get_small_thumb())
    embed.set_footer(text="Data provided by IGDB")

    log.debug(f"Title: {games[0].get_title()}")
    log.debug(f"Small Thumb: {games[0].get_small_thumb()}")
    log.debug(f"Developer: {games[0].get_developer()}")
    log.debug(f"Publisher: {games[0].get_publisher()}")
    log.debug(f"Release Date: {convert_date(games[0].get_release_date())}")

    return embed
