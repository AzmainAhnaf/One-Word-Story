import discord
limit = 10

def get_story(file: str) -> str:
    story = ""
    count = 0
    with open(file, "r", encoding="utf-8") as file:
        for line in file:
            story = story + line[:-1] + " "
            count += 1

    # Checking the len of the story
    if (count < limit):
        return f"The story has {count} words, make at least {limit} words to complete the story"
    
    # Deleting the story
    with open("story.txt", "w") as file:
        pass
    return story