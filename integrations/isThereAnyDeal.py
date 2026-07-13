import requests, json
from config.env import ITAD_TOKEN

ITAD_BASE_URL = "https://api.isthereanydeal.com"
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

    
    price_r = requests.post(
        f"{ITAD_BASE_URL}/games/overview/v2",
        params={"deals": True},
        json=[itad_id],
        headers=auth_header,
    )
    price_data = json.loads(price_r.text)
    
    current_price = {
        "amount": price_data["prices"][0]["current"]["price"]["amount"],
        "cut": price_data["prices"][0]["current"]["cut"],
    }
    hist_low = {
        "amount": price_data["prices"][0]["lowest"]["price"]["amount"],
        "cut": price_data["prices"][0]["lowest"]["cut"]
    }
    
    return current_price, hist_low
        
