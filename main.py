import logging
import threading
import nextcord
from nextcord.ext import commands

from logger import setup_logging
from core.health_handler import run_health_server
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
    from commands import gsearch_command

    result = gsearch_command(query)

    """
    Assign those later so we can have a fallback if results is None.
    If no game matches the query, the game list will be a "None" list, therefore
    python will try to iterate on it, throwing an error. So we only assign a value
    if there's valid results. See commands.py:17
    """
    embed, menu = result if result is not None else (None, None)

    if embed is not None:
        await ctx.send(embed=embed)
        await ctx.send(view=menu)
    else:
        no_results = nextcord.Embed(
            title="No Games Found",
            description="No games matched your search. Try a different title or check your spelling.",
            color=nextcord.Color.red(),
        )
        await ctx.send(embed=no_results)


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
