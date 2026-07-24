import json


def test_igdb_games_response_json_factory_returns_valid_igdb_payload(
    igdb_games_response_json,
):
    payload = json.loads(igdb_games_response_json())

    assert payload == [
        {
            "id": 10763,
            "cover": {
                "id": 117991,
                "url": "//images.igdb.com/igdb/image/upload/t_thumb/co2j1j.jpg",
            },
            "first_release_date": 1159228800,
            "involved_companies": [
                {
                    "id": 84780,
                    "company": {
                        "id": 21848,
                        "name": "SuperTuxKart Development Team",
                    },
                    "developer": True,
                    "publisher": True,
                }
            ],
            "name": "SuperTuxKart",
            "slug": "supertuxkart",
            "external_games": [
                {"id": 113287, "external_game_source": {"id": 3, "name": "GiantBomb"}}
            ],
        }
    ]


def test_igdb_games_response_factory_returns_independent_payloads(
    igdb_games_response,
):
    first_payload = igdb_games_response()
    second_payload = igdb_games_response()

    first_payload[0]["name"] = "Changed"

    assert second_payload[0]["name"] == "SuperTuxKart"
