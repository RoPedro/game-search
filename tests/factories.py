import json
from copy import deepcopy
from typing import Any


def igdb_company_factory(**overrides: Any) -> dict[str, Any]:
    company = {
        "id": 21848,
        "name": "SuperTuxKart Development Team",
    }
    company.update(overrides)
    return company


def igdb_involved_company_factory(**overrides: Any) -> dict[str, Any]:
    involved_company = {
        "id": 84780,
        "company": igdb_company_factory(),
        "developer": True,
        "publisher": True,
    }
    involved_company.update(overrides)
    return involved_company


def igdb_external_games_factory(**overrides: Any) -> dict[str, Any]:
    # fmt: off
    external_game = {
        "id": 113287,
        "external_game_source": {
            "id": 3,
            "name": "GiantBomb"
        }
    }
    # fmt: on
    external_game.update(overrides)
    return external_game


def igdb_cover_factory(**overrides: Any) -> dict[str, Any]:
    cover = {
        "id": 117991,
        "url": "//images.igdb.com/igdb/image/upload/t_thumb/co2j1j.jpg",
    }
    cover.update(overrides)
    return cover


def igdb_game_factory(**overrides: Any) -> dict[str, Any]:
    game = {
        "id": 10763,
        "cover": igdb_cover_factory(),
        "first_release_date": 1159228800,
        "involved_companies": [igdb_involved_company_factory()],
        "name": "SuperTuxKart",
        "slug": "supertuxkart",
        "external_games": [igdb_external_games_factory()],
    }
    game.update(overrides)
    return game


def igdb_games_response_factory(
    games: list[dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    if games is None:
        games = [igdb_game_factory()]
    return deepcopy(
        games
    )  # A separate copy of the base game factory it's reusable in multiple different tests.


def igdb_games_response_json_factory(
    games: list[dict[str, Any]] | None = None,
) -> str:
    return json.dumps(igdb_games_response_factory(games))
