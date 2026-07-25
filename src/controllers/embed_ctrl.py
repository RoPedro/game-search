from core.utils import build_prices_embed
from models.embeds import deals_not_found


async def send_prices(ctx, result):
    prices = await build_prices_embed(result[0])
    if prices is not "" and prices is not None:
        await ctx.send(embed=prices)
    else:
        await ctx.send(embed=deals_not_found)
