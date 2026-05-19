from dotenv import load_dotenv
import json

from core.utils import build_embed, create_games_array
from core.igdb_auth import wrapper

load_dotenv()


def gsearch_command(query: str):
    LIMIT = 4
    game_response = wrapper.api_request(
        "games",
        f'fields name, involved_companies.company.name, involved_companies.developer, involved_companies.publisher, first_release_date, cover.url; search "{query}"; where game_type = 0; limit {LIMIT};',
    )
    igdb_data = json.loads(game_response)
    if igdb_data == []:
        return None
    
    games = create_games_array(igdb_data, limit=LIMIT)
    embed = build_embed(games)
    return embed
