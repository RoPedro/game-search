import pytest

from tests.factories import (
    igdb_company_factory,
    igdb_cover_factory,
    igdb_game_factory,
    igdb_external_games_factory,
    igdb_games_response_factory,
    igdb_games_response_json_factory,
    igdb_involved_company_factory,
)


@pytest.fixture
def igdb_company():
    return igdb_company_factory


@pytest.fixture
def igdb_cover():
    return igdb_cover_factory


@pytest.fixture
def igdb_game():
    return igdb_game_factory


@pytest.fixture
def igdb_external_games():
    return igdb_external_games_factory


@pytest.fixture
def igdb_games_response():
    return igdb_games_response_factory


@pytest.fixture
def igdb_games_response_json():
    return igdb_games_response_json_factory


@pytest.fixture
def igdb_involved_company():
    return igdb_involved_company_factory
