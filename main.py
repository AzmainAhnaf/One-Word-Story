import os
from dotenv import load_dotenv
import discord
from story import get_story, add_word, get_story_force
from setup import get_id, set_id

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
    # print(message.content)

    # Cheking if the message was sent by the bot itself
    if (message.author == client.user):
        return
    
    # checking if the user has admin privileges
    is_admin: bool = message.author.top_role.permissions.administrator
    
    # setting up the text channel
    if (message.content.lower().startswith("?settextchannel")):
        if is_admin:
            status: int = set_id(message)
            if status == 1:
                await message.channel.send("```\nuse ?settextchannel [text channel id]\n```")
            elif status == 2:
                await message.channel.send("```\nToo much arguments provided\n```")
            elif status == 0:
                await message.add_reaction("✅")
        else:
            await message.channel.send("```\nYou are not authorized to use this command\n```")
    
    # setting new limit
    if (message.content.lower().startswith("?changelimit")):
        if is_admin:
            status: int = set_id(message)
            print(status)
            if status == -1:
                # no argument is given
                await message.channel.send("```\nuse ?changelimit [number]")
            elif status == -2:
                # Too much argument is given
                await message.channel.send("```\ntoo much argument\n```")
            elif status == -3:
                await message.channel.send("```\nargument is not an integer\n```")
            elif status == -4:
                await message.channel.send("```\nargument is not a non-positive integer\n```")
            else:
                await message.channel.send(f"```\nnew limit is set to {status}\n```")
        else:
            await message.channel.send("```\nYou are not authorized to use this command\n```")
        return

    # Getting text channel id
    text_channel_id: str = get_id()

    if (str(message.channel.id).strip() == text_channel_id.strip()):
        if (message.content.lower() == "?makestory"):
            await message.channel.send("```\n" + get_story("story.txt") + "\n```")
        elif (message.content.lower() == "?forcemakestory"):
            # Checking if the user has administrative permission
            if is_admin:
                await message.channel.send("```\n" + get_story_force("story.txt") + "\n```")
                check = True
            else:
                await message.channel.send("```\nYou are not authorized to use this command\n```")
        else:
            state: bool = add_word(message, "story.txt") # checking if the word was added to story
            if (state):
                await message.add_reaction("✅")
            else:
                await message.add_reaction("❌")
    elif message.content.startswith("?"):
        await message.channel.send("```\nuse ?settextchannel [channel id] to set your text channel\n```")
        

    
# Main entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()