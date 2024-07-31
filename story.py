import discord
from setup import get_limit

# minimum length of the story
limit = get_limit()

# Creating story regardless of it's length
def get_story_force(file: str) -> str:
    story = ""
    with open(file, "r", encoding="utf-8") as words:
        for word in words:
            story = story + word[:-1] + " "
    
    # Checking if the len of the story is 0
    if (len(story) == 0):
        return "The story has no words in it"
    
    # deleting contents of story and user
    with open("story.txt", "w") as _:
        pass
    with open("user.txt", "w") as _:
        pass

    return story


# Compiling story and checking minimum length of the story
def get_story(file: str) -> str:
    # getting the limit
    limit = get_limit()
    story = ""
    count = 0
    # Compiling story from txt file
    with open(file, "r", encoding="utf-8") as words:
        for word in words:
            story = story + word[:-1] + " "
            count += 1

    # Checking the len of the story
    if (count < limit):
        return f"The story has {count} words, make at least {limit} words to complete the story"
    
    # Deleting the story and users
    with open(file, "w") as words:
        pass
    with open("user.txt", "w") as usernames:
        pass
    return story

# getting all the users that have contributed in the storymaking
def get_user(file: str) -> list:
    users = []
    with open(file, "r", encoding="utf-8") as usernames:
        for user in usernames:
            users.append(user)
    return users

# Adding words to the story and user to the user.txt
def add_word(message: discord.Message, file: str) -> bool:
    # Collecting message informations
    user_id = str(message.author)
    content = message.content
    content = content.split()

    # Checking if user has typed multiple words
    if (len(content) > 1):
        return False
    
    content = content[0]
    
    # getting latest_user list
    latest_user = get_user("user.txt")
    current_user = str(user_id)

    # Checking if the user is eligible to append to story
    if (len(latest_user) == 0):
        with open(file, "a", encoding="utf-8") as story:
            story.write(content + "\n")
        with open("user.txt", "a", encoding="utf-8") as users:
            users.write(user_id + "\n")
        return True
    elif (current_user.strip() == latest_user[-1].strip()):
        print("returned false")
        return False
    else:
        print("returned true")
        with open(file, "a", encoding="utf-8") as story:
            story.write(content + "\n")
        with open("user.txt", "a", encoding="utf-8") as users:
            users.write(user_id + "\n")
        return True
