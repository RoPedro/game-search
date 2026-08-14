import logging
import nextcord

from core.utils import convert_date
from src.models.embeds import deals_not_found, invalid_itad_key, unknown_error
from config.env import lang_data
from integrations.isThereAnyDeal import get_itad_price, ITAD_BASE_WEB_URL
from config.env import lang_data, ITAD_TOKEN

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


def prices_embed_template(current_price, hist_low, hist_low_cut: int):
    embed = nextcord.Embed(
        title=lang_data["pricesEmbed"]["title"],
        # fmt: off
        description=f"{lang_data["pricesEmbed"]["currentPrice"]}: {current_price["amount"]} ({current_price["cut"]}%)\n"
                    f"{lang_data["pricesEmbed"]["historicalLow"]}: {hist_low["amount"]} ({hist_low_cut}%)",
        # fmt: on
    )
    return embed


async def send_prices(ctx, result):
    prices = await build_prices_embed(result[0])
    
    if isinstance(prices, nextcord.Embed):
        await ctx.send(embed=prices)
    elif prices == 403:  # API Response to invalid key
        await ctx.send(embed=invalid_itad_key)
    elif isinstance(prices, int):
        await ctx.send(embed=unknown_error)
    else:  # Triggers mainly when ITAD connects, but no deals is found (e.g. Switch games)
        await ctx.send(embed=deals_not_found)


async def build_prices_embed(games):
    result = get_itad_price(games.get_external_id(), ITAD_TOKEN)
    log.debug(f"ITAD Result: {result}")

    if isinstance(result, int):
        return result
    if not result or result == "":
        log.warning(f"isThereAnyDeal returned None, No deals found")
        return None

    current_price = result[0]  # 0 = Current Price
    hist_low = result[1]  # 1 = Historical Low
    regular_price = result[2]  # 2 = Regular Price
    slug = result[3]  # 3 = Slug
    cut = (
        (regular_price - float(hist_low["amount"])) / regular_price
    ) * 100  # Get discount amount in %

    prices_embed = prices_embed_template(current_price, hist_low, int(cut))
    prices_embed.add_field(
        name=lang_data["pricesEmbed"]["detailedPricesHeader"],
        value=f"{ITAD_BASE_WEB_URL}/game/{slug}",
    )
    prices_embed.set_footer(text=lang_data["pricesEmbed"]["dealsFooter"])

    return prices_embed
