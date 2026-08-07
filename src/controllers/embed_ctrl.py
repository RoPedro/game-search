import logging
import nextcord

from core.utils import convert_date
from src.models.embeds import deals_not_found
from config.env import lang_data
from integrations.isThereAnyDeal import get_itad_price, ITAD_BASE_WEB_URL
from config.env import lang_data

log = logging.getLogger(__name__)


def build_embed(games):
    embed = game_embed_template(games)
    embed.set_image(url=games[0].get_small_thumb())
    embed.set_footer(text=lang_data["gameEmbed"]["embedFooter"])

    log.debug(f"Title: {games[0].get_title()}")
    log.debug(f"Small Thumb: {games[0].get_small_thumb()}")
    log.debug(f"Developer: {games[0].get_developer()}")
    log.debug(f"Publisher: {games[0].get_publisher()}")
    log.debug(f"Release Date: {convert_date(games[0].get_release_date())}")

    return embed


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
    if prices != "" and prices is not None:
        await ctx.send(embed=prices)
    else:
        await ctx.send(embed=deals_not_found)


async def build_prices_embed(games):
    result = get_itad_price(games.get_external_id())

    if not result or result == "":
        return None

    current_price = result[0]  # 0 = Current Price
    hist_low = result[1]  # 1 = Historical Low
    slug = result[2]  # 2 = Slug

    prices_embed = prices_embed_template(current_price, hist_low)
    prices_embed.add_field(
        name=lang_data["pricesEmbed"]["detailedPricesHeader"],
        value=f"{ITAD_BASE_WEB_URL}/game/{slug}",
    )
    prices_embed.set_footer(text=lang_data["pricesEmbed"]["dealsFooter"])

    return prices_embed
