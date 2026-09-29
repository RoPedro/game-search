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

28/09/2026 - Added a fallback in case the valid external ID is not the first one.
This can consume 2/3 extra API calls from ITAD for each `gsearch_command()`, for
now, it's manageable, but it may be removed later, especially if IGDB adds better
filtering of inactive games, see:
https://twitch.uservoice.com/forums/929953-igdb/suggestions/51715681-add-a-status-field-to-external-games-to-indicate

## Resident Evil 4 2005 (DEAL NOT FOUND)
Behavior: Does not find deals, even being a PC game
Status: Investigating