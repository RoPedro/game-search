import logging

from src.models.game import Game

log = logging.getLogger(__name__)


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
