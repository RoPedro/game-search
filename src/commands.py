from dotenv import load_dotenv
import json

from core.utils import build_embed, create_games_array, build_menu
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
            )
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

    games = create_games_array(igdb_data, limit=LIMIT)
    embed = build_embed(games)
    menu = build_menu(games)
    return embed, menu


# A background command that the user should only access by other functions such as gamesearch
def slug_search_command(query: str):
    game_response = wrapper.api_request(
        "games",
        f'fields name, slug, involved_companies.company.name, involved_companies.developer, involved_companies.publisher, first_release_date, cover.url; where slug = "{query}";',
    )
    igdb_data = json.loads(game_response)
    if igdb_data == []:
        return None

    game = create_games_array(igdb_data, 1)  # Send 1 for limit since it's only one game
    embed = build_embed(game)
    return embed
