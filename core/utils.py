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
    for i in range(limit):
        try:
            game = Game( # iterate with i because igdb games list don't have a "game" key, so number instead.
                title=igdb_data[i]["name"],
                developer=igdb_data[i]["involved_companies"][0]["company"]["name"],
                release_date=igdb_data[i]["first_release_date"],
                small_thumb="https:" + igdb_data[i]["cover"]["url"].replace(
                    "t_thumb", "t_cover_big"
                ),
            )
            games.append(game)
        except (IndexError, KeyError):
            continue
    return games

def build_embed(games):
    embed = Embed(
        title=games[0].get_title(),
        description=f"Developer: {games[0].get_developer()}\nRelease Date: {convert_date(games[0].get_release_date())}",
    )
    embed.set_image(url=games[0].get_small_thumb())
    embed.set_footer(text="Data provided by IGDB")

    print(f"Title: {games[0].get_title()}")
    print(f"Small Thumb: {games[0].get_small_thumb()}")
    print(f"Developer: {games[0].get_developer()}")
    print(f"Release Date: {convert_date(games[0].get_release_date())}")

    return embed