from datetime import datetime
from models.game import Game
from nextcord import Embed


# Don't crash if date is invalid
def convert_date(date_stamp):
    if date_stamp is None:
        return "Unknown"
    try:
        return datetime.fromtimestamp(date_stamp).strftime("%d/%m/%Y")
    except ValueError:
        return None


def create_games_array(igdb_data, limit=4):
    games = []
    for game in range(limit): # Limit = number of games to show, default is 4.
        try:
            data_developer, data_publisher = find_set_companies(
                igdb_data[game]
            )  # send the index so it knows what game is. (data[game_index])
            game = Game(  # iterate with game because igdb games list don't have a "game" key, so number instead.
                title=igdb_data[game]["name"],
                developer=data_developer,
                publisher=data_publisher,
                release_date=igdb_data[game]["first_release_date"],
                small_thumb="https:"
                + igdb_data[game]["cover"]["url"].replace("t_thumb", "t_cover_big"),
            )
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


def build_embed(games):
    embed = Embed(
        title=games[0].get_title(),
        description=f"Developer: {games[0].get_developer()}\nPublisher: {games[0].get_publisher()}\nRelease Date: {convert_date(games[0].get_release_date())}",
    )
    embed.set_image(url=games[0].get_small_thumb())
    embed.set_footer(text="Data provided by IGDB")

    print(f"Title: {games[0].get_title()}")
    print(f"Small Thumb: {games[0].get_small_thumb()}")
    print(f"Developer: {games[0].get_developer()}")
    print(f"Publisher: {games[0].get_publisher()}")
    print(f"Release Date: {convert_date(games[0].get_release_date())}")

    return embed
