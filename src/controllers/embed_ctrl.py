import nextcord

from core.utils import build_prices_embed
from src.models.embeds import deals_not_found


def prices_embed_template(current_price, hist_low):
    embed = nextcord.Embed(
        title="💸Deals and price💸",
        description=f"Current Price: {current_price["amount"]} ({current_price["cut"]}%)\n"
        f"Historical Low: {hist_low["amount"]} ({hist_low["cut"]}%)",
    )
    return embed


async def send_prices(ctx, result):
    prices = await build_prices_embed(result[0])
    if prices is not "" and prices is not None:
        await ctx.send(embed=prices)
    else:
        await ctx.send(embed=deals_not_found)
