import requests
from os import getenv
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands


load_dotenv()

TOKEN = getenv("TOKEN")

# Define intents so it can read message content (required for commands to work)
intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="?", intents=intents)


@bot.command(name="gsearch", description="Search for a game by its name")
async def gsearch(ctx, *, query: str):
    from commands import gsearch_command

    embed = gsearch_command(query)
    await ctx.send(embed=embed)


if bot.run(str(TOKEN)):
    print("Bot is running!")
