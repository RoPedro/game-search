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

def deals_not_found_template(title_slug):
    embed = nextcord.Embed(  # TODO: Create error embeds in separate places
        title=lang_data["dealsNotFound"]["title"],
        description=lang_data["dealsNotFound"]["description"],
        color=nextcord.Color.red(),
    )
    embed.add_field(
        name=lang_data["dealsNotFound"]["linkTip"],
        value=f"https://google.com/search?q=isthereanydeal-{title_slug}"
    )
    return embed


def prices_embed_template(current_price, hist_low, hist_low_cut: int):
    embed = nextcord.Embed(
        title=lang_data["pricesEmbed"]["title"],
        # fmt: off
        description=f"{lang_data["pricesEmbed"]["currentPrice"]}: {current_price["amount"]} ({current_price["cut"]}%)\n"
                    f"{lang_data["pricesEmbed"]["historicalLow"]}: {hist_low["amount"]} ({hist_low_cut}%)",
        # fmt: on
    )
    return embed
