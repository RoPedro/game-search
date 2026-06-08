from core.utils import create_games_array, find_set_companies
from models.game import Game


def test_find_set_companies_returns_developer_and_publisher(
    igdb_company,
    igdb_game,
    igdb_involved_company,
):
    game = igdb_game(
        involved_companies=[
            igdb_involved_company(
                company=igdb_company(name="Publisher Studio"),
                developer=False,
                publisher=True,
            ),
            igdb_involved_company(
                company=igdb_company(name="Developer Studio"),
                developer=True,
                publisher=False,
            ),
        ]
    )

    developer, publisher = find_set_companies(game)

    assert developer == "Developer Studio"
    assert publisher == "Publisher Studio"


def test_create_games_array_maps_igdb_payload_to_games(
    monkeypatch,
    igdb_games_response,
):
    def fake_find_dominant_color(self):
        self.dominant_color = "0x123456"

    monkeypatch.setattr(Game, "find_dominant_color", fake_find_dominant_color)

    games = create_games_array(igdb_games_response(), limit=1)

    assert len(games) == 1
    assert games[0].get_title() == "SuperTuxKart"
    assert games[0].get_slug() == "supertuxkart"
    assert games[0].get_developer() == "SuperTuxKart Development Team"
    assert games[0].get_publisher() == "SuperTuxKart Development Team"
    assert games[0].get_release_date() == 1159228800
    assert games[0].get_small_thumb() == (
        "https://images.igdb.com/igdb/image/upload/t_1080p/co2j1j.jpg"
    )
    assert games[0].get_dominant_color() == "0x123456"
