import json


def itad_valid_prices_payload():
    payload = [
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

    return json.dumps(payload)
