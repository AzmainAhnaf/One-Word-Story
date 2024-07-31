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

def get_limit() -> int:
    limit = 0
    with open("limit.txt", "r") as limit_file:
        for line in limit_file:
            limit = line
    limit = int(limit.strip())
    return limit

# Setting the limit of words and handling exceptions
def set_limit(message: discord.Message) -> int:
    messages = message.content.split()
    print(messages)
    if (len(messages) == 1):
        return -1 # No argument
    elif (len(messages) > 2):
        return -2 # Too much argument
    elif (len(messages) == 2):
        new_limit = messages[1]
        if (new_limit.isnumeric()):
            new_limit = int(new_limit)
            if new_limit < 1:
                return -4 # Non-positive limit
            else:
                with open("limit.txt", "w") as limit_file:
                    limit_file.write(new_limit)
                    return new_limit
        else:
            return -3 # Argument is not an integer
