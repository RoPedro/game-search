import logging
import threading
from os import getenv
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands

from logger import setup_logging
from core.health_handler import run_health_server

# Thread the health server so it crashes gracefully with the main process
threading.Thread(target=run_health_server, daemon=True).start()

setup_logging()
log = logging.getLogger(__name__)

load_dotenv()

ENV = getenv("ENV")
TOKEN = getenv("TOKEN")

# Define intents so it can read message content (required for commands to work)
intents = nextcord.Intents.default()
intents.message_content = True

prefix = ""
if ENV == "production":
    prefix = "?"
elif ENV == "development":
    prefix = "."

bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.command(name="gs", description="Search for a game by its name")
async def gsearch(ctx, *, query: str):
    from commands import gsearch_command

    embed = gsearch_command(query)
    await ctx.send(embed=embed)


bot.run(str(TOKEN))
