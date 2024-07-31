import os
from dotenv import load_dotenv
import discord

# Loading Token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Setting bot and it's intents
intents: discord.Intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True
client: discord.Client = discord.Client(intents=intents)