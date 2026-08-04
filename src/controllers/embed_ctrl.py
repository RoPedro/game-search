import nextcord

from core.utils import build_prices_embed, convert_date
from src.models.embeds import deals_not_found
from config.env import lang_data


def game_embed_template(games):
    embed = nextcord.Embed(
        title=games[0].get_title(),
        # fmt: off
        description=f"{lang_data["gameEmbed"]["developerField"]}: {games[0].get_developer()}\n"
                    f"{lang_data["gameEmbed"]["publisherField"]}: {games[0].get_publisher()}\n"
                    f"{lang_data["gameEmbed"]["releaseDateField"]}: {convert_date(games[0].get_release_date())}",
        # fmt: on
        colour=int(
            games[0].get_dominant_color(), 16
        ),  # Need to specify 16 since we're passing a hexadecimal string
    )
    return embed


def prices_embed_template(current_price, hist_low):
    embed = nextcord.Embed(
        title=lang_data["pricesEmbed"]["title"],
        # fmt: off
        description=f"{lang_data["pricesEmbed"]["currentPrice"]}: {current_price["amount"]} ({current_price["cut"]}%)\n"
                    f"{lang_data["pricesEmbed"]["historicalLow"]}: {hist_low["amount"]}",
        # fmt: on
    )
    return embed


async def send_prices(ctx, result):
    prices = await build_prices_embed(result[0])
    if prices is not "" and prices is not None:
        await ctx.send(embed=prices)
    else:
        await ctx.send(embed=deals_not_found)
