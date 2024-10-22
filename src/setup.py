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

def set_id(message: str) -> int:
    messages = message.lower().split()
    # Handling excpetions and setting text channel
    if len(messages) == 1:
        return 1 # No arguments
    elif len(messages) > 2:
        return 2 # Too much arguments
    else:
        id = messages[1].strip()
        with open("channel_id.txt", "w") as file:
            file.write(id + "\n")
        return 0 # Used correctly
    return

def get_limit() -> int:
    limit = 0
    with open("limit.txt", "r") as limit_file:
        for line in limit_file:
            limit = line
    limit = int(limit.strip())
    return limit

# Setting the limit of words and handling exceptions
def set_limit(message: str) -> int:
    messages = message.lower().split()
    # print(messages)
    if (len(messages) == 1):
        return -1 # No argument
    elif (len(messages) > 2):
        return -2 # Too much argument
    elif (len(messages) == 2):
        new_limit = messages[1]
        if (new_limit.isnumeric()):
            new_limit = int(new_limit)
            if new_limit == 0:
                return -4 # zrgument is 0
            else:
                with open("limit.txt", "w") as limit_file:
                    limit_file.write(str(new_limit))
                    return new_limit
        else:
            return -3 # Argument is not a positive integer
