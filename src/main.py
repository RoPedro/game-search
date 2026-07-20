import logging
import threading
import asyncio
import nextcord
from nextcord.ext import commands

from core.health_handler import run_health_server
from core.utils import build_embed, build_menu
from models.embeds import game_not_found
from src.controllers.embed_ctrl import send_prices
from config.logger import setup_logging
from config.env import TOKEN, prefix

# Thread the health server so it crashes gracefully with the main process
threading.Thread(target=run_health_server, daemon=True).start()

setup_logging()
log = logging.getLogger(__name__)

# Define intents so it can read message content (required for commands to work)
intents = nextcord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.command(name="gs", description="Search for a game by its name")
@commands.cooldown(1, 5, lambda message: message.author.id)
async def gsearch(ctx, *, query: str):
    """
    According to Nextcord issue [#1282](https://github.com/nextcord/nextcord/issues/1282), cooldowns for non-slash commands are broken.
    Tipically we would use @commands.cooldown(x, y, BucketType.user), which returns message.author.id. Since not working, we use lambda instead.
    Lambda works because cooldown() only blocks BucketType, so we bypass by getting the author ID directly from the message object.
    """
    from src.commands import gsearch_command

    result = gsearch_command(query)

    """
    Assign those later so we can have a fallback if results is None.
    If no game matches the query, the game list will be a "None" list, therefore
    python will try to iterate on it, throwing an error. So we only assign a value
    if there's valid results. See commands.py:17
    """

    if result is not None:
        embed = build_embed(result)
        menu = build_menu(result)
        
        await ctx.send(embed=embed)
        await ctx.send(view=menu)

        asyncio.create_task(send_prices(ctx, result))
    else:
        log.error(f"Result returned as: {result}. If it is None, probably a invalid game")
        await ctx.send(embed=game_not_found)


@bot.event
async def on_command_error(ctx, error):
    error = getattr(error, "original", error)
    if isinstance(error, commands.CommandOnCooldown):
        cd_embed = nextcord.Embed(
            title="🤚 Command on Cooldown 🤚",
            description=f"Please wait {error.retry_after:.1f} seconds before using this command again.",
            color=nextcord.Color.orange(),
        )
        await ctx.send(embed=cd_embed)
    else:  # Unhandled errors get suppressed if not logged.
        log.error("Unhandled command error", exc_info=error)


bot.run(str(TOKEN))
