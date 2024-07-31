import os
from dotenv import load_dotenv
import discord
from story import get_story

# Loading Token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Setting bot and it's intents
intents: discord.Intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True
client: discord.Client = discord.Client(intents=intents)

# Booting up the bot
@client.event
async def on_ready():
    print(f"{client.user} has logged in")

# Handling messages
@client.event
async def on_message(message: discord.Message) -> None:
    if (message.author == client.user):
        return
    
    if (message.channel.id == 1268158484231356447):
        if (message.content == "?makestory"):
            await get_story("story.txt")
        else:
            pass # implement add_word

    
# Main entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()