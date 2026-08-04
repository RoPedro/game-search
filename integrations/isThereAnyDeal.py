import requests, json
from config.env import ITAD_TOKEN, LANG

ITAD_BASE_URL = "https://api.isthereanydeal.com"
ITAD_BASE_WEB_URL = "https://isthereanydeal.com"
ITAD_ICON = "https://isthereanydeal.com/public/assets/logo-GBHE6XF2.svg"
ITAD_GAME_LOOKUP_URL = ""
auth_header = {"ITAD-API-Key": ITAD_TOKEN}


def get_itad_price(external_id):
    r = requests.get(
        f"{ITAD_BASE_URL}/games/lookup/v1",
        params={"appid": external_id},
        headers=auth_header,
    )

    game_data = json.loads(r.text)
    if game_data["found"] == False:
        return ""
    itad_id = game_data["game"]["id"]
    itad_slug = game_data["game"]["slug"]

    price_r = requests.post(
        f"{ITAD_BASE_URL}/games/prices/v3",
        params={"country": LANG},
        json=[itad_id],
        headers=auth_header,
    )
    price_data = json.loads(price_r.text)

    current_price = {
        "amount": price_data[0]["deals"][0]["price"]["amount"],
        "cut": price_data[0]["deals"][0]["cut"],
    }
    hist_low = {
        "amount": price_data[0]["historyLow"]["y1"]["amount"],
    }

    return current_price, hist_low, itad_slug
