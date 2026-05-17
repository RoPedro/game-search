import logging
from os import getenv
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands

from logger import setup_logging

setup_logging()
log = logging.getLogger(__name__)

load_dotenv()

TOKEN = getenv("TOKEN")

# Define intents so it can read message content (required for commands to work)
intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="?", intents=intents)


@bot.command(name="gs", description="Search for a game by its name")
async def gsearch(ctx, *, query: str):
    from commands import gsearch_command

    embed = gsearch_command(query)
    await ctx.send(embed=embed)


bot.run(str(TOKEN))
