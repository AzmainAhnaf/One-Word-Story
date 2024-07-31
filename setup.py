import discord

# Setting up channel id
def get_id() -> str:
    id = []
    with open("channel_id.txt", "r") as file:
        for line in file:
            id.append(line)
    if (len(id) == 0):
        return "Not Found"
    id = id[0].strip()
    return str(id).strip()

def set_id(message: discord.Message) -> int:
    messages = message.content.split()
    # Handling excpetions and setting text channel
    if len(messages) == 1:
        return 1 
    elif len(messages) > 2:
        return 2
    else:
        id = messages[1].strip()
        with open("channel_id.txt", "w") as file:
            file.write(id + "\n")
        return 0 #await message.add_reaction("✅")
    return
