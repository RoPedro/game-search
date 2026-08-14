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


def test_itad_valid_response_returns_valid_payloadd(
    itad_valid_response_json,
):
    payload = json.loads(itad_valid_response_json())

    assert payload == [
        {
            "id": "018d937f-33f0-7200-80fc-87f769196c84",
            "historyLow": {
                "all": {"amount": 6.24, "amountInt": 624, "currency": "USD"},
                "y1": {"amount": 6.24, "amountInt": 624, "currency": "USD"},
                "m3": {"amount": 6.24, "amountInt": 624, "currency": "USD"},
            },
            "deals": [
                {
                    "shop": {"id": 61, "name": "Steam"},
                    "price": {"amount": 24.99, "amountInt": 2499, "currency": "USD"},
                    "regular": {"amount": 24.99, "amountInt": 2499, "currency": "USD"},
                    "cut": 0,
                    "voucher": None,
                    "storeLow": {"amount": 6.24, "amountInt": 624, "currency": "USD"},
                    "flag": None,
                    "drm": [],
                    "platforms": [
                        {"id": 1, "name": "Windows"},
                        {"id": 2, "name": "Mac"},
                    ],
                    "timestamp": "2026-07-27T19:34:46+02:00",
                    "expiry": None,
                    "url": "https://itad.link/018d9386-712c-707d-bd4d-e2329c84b026/",
                }
            ],
        }
    ]
