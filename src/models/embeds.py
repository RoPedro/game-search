# All fixed embeds (like error embeds) will be stored here

import nextcord

from config.env import lang_data

game_not_found = nextcord.Embed(
    title=lang_data["gameNotFound"]["title"],
    description=lang_data["gameNotFound"]["description"],
    color=nextcord.Color.red(),
)

# Mainly for when isThereAnyDeal returns 40x, but not 403.
unknown_error = nextcord.Embed(
    title=lang_data["embeds"]["unknownError"]["title"],
    description=lang_data["embeds"]["unknownError"]["description"],
    color=nextcord.Color.red(),
)

invalid_itad_key = nextcord.Embed(
    title=lang_data["embeds"]["invalidApiKey"]["title"],
    description=lang_data["embeds"]["invalidApiKey"]["description"],
    color=nextcord.Color.red(),
)

deals_not_found = nextcord.Embed(  # TODO: Create error embeds in separate places
    title=lang_data["dealsNotFound"]["title"],
    description=lang_data["dealsNotFound"]["description"],
    color=nextcord.Color.red(),
)
