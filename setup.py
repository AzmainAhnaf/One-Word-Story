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
