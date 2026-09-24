## Dragon Ball FighterZ (DEAL NOT FOUND)
Behavior: Does not find deals, even being a PC game
Issue: IGDB has 2(two) entries for `external_games` from Steam, and the second entry is the valid one.
```json
{
    "id": 3183491,
    "uid": "1725510", # <-- Inactive Steam UID
    "external_game_source": {
        "id": 1,
        "name": "Steam"
    }
},
{
    "id": 214838,
    "uid": "678950",
    "external_game_source": {
        "id": 1,
        "name": "Steam"
    }
},
```
Status: Not fixed yet, added manual search to embed.

## Resident Evil 4 2005 (DEAL NOT FOUND)
Behavior: Does not find deals, even being a PC game
Status: Investigating