from dotenv import load_dotenv
import json

from src.controllers.embed_ctrl import build_embed
from src.controllers import game_ctrl
from core.igdb_auth import wrapper
from integrations.igdb import getFields

load_dotenv()


def gsearch_command(query: str):
    LIMIT = 5
    query_fields = getFields()

    if query.endswith("remake") or query.endswith("remaster"):
        query = query.removesuffix("remake").removesuffix("remaster").strip()
        game_response = wrapper.api_request(
            "games",
            (
                f"fields {query_fields};"
                f'search "{query}";'
                f"where game_type = (0, 8, 9);"
                f"limit {LIMIT};"
            ),
        )
    else:
        game_response = wrapper.api_request(
            "games",
            (
                f"fields {query_fields};"
                f'search "{query}";'
                f"where game_type = 0;"
                f"limit {LIMIT};"
            ),
        )

    igdb_data = json.loads(game_response)
    if igdb_data == []:
        return None

    games = game_ctrl.create_games_array(igdb_data, limit=LIMIT)

    # TODO: Study the possibility of wrapping all those functions into one `build_user_response`
    # Update, probably not viable since performance is not as I want to be
    return games


# A background command that the user should only access by other functions such as gamesearch
def slug_search_command(query: str):
    query_fields = getFields()
    game_response = wrapper.api_request(
        "games", (f"fields {query_fields};" f'where slug = "{query}";')
    )

    igdb_data = json.loads(game_response)
    if igdb_data == []:
        return None

    game = game_ctrl.create_games_array(igdb_data, 1)  # Send 1 for limit since it's only one game
    embed = build_embed(game)
    return embed
