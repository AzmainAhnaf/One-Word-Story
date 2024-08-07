# One Word Story Bot

<br>

## TL;DR
The program is a functional discord bot that creates story from words given by the users of the server

<br>

## Table of Contents
- [TL;DR](#tldr)
- [Setting up bot in your server](#setting-up-the-bot-in-your-server)
- [Bot Commands Functionality](#bot-commands-functionlity)
- [Programme Files Explaination](#programme-files-explaination)
- [Programme Explaination](#programme-explaination)

<br>

## Setting up the bot in your server

### Step 1: Making your own bot
Go to [Discord Developer Portal](https://www.discord.com/developers/applications) and create your own bot from their
if you are having trouble, you can watch this [Youtube video](https://www.youtube.com/watch?v=UYJDKSah-Ww)
from 2:24 to 6:30. Collect your token

### Step 2: Clone the repository
Clone this repository and inside the .env file, insert your bot token

### Step 3: Run your bot
Run your bot locally from your machine or use any cloud service that you are comfortable with

<br>

## Bot Commands Functionlity
### ?settextchannel \[text_channel_id\]
use ?settextchannel in the above mentioned way to set the text channel where the bot will collect words from and show the story it has compiled so far. This command can only be used if the user has administrator permission.

### ?makestory
use ?makestory to compile the story from so far collected words. This function only works if the word limit has reached the minimum_limit

### ?forcemakestory
use ?forcemakestory to compile the story regardless of minimum world limit, this command can only work if you have administrator privilege in the server

### ?changelimit \[number\]
change the minimum word limit of your bot, by default, the limit is set to 10

### ?help
use ?help to get the online documentation and also how to setup text channel in one's server

<br>

## Programme files explaination

### main.py
this is where the whole programme come together and act as one single entity, the story bot

### story.py
this python file stores the function of adding words to the and story and compiling story, detailed explanation is given below

### setup.py
this python file helps setup the bot with channel_id and limit.

### test_setup.py
this python file tests the functions of setup.py using pytest library

### story.txt
this is the .txt file where all the words are kept stored for the next story compilation

### user.txt
this is the .txt file where the order of the user is maintained, this helps checking if a user is sending more than one words consecutively

### limit.txt
the minimum word count is stored here and changed when the ?changelimit command is used

### channel_id.txt
this is where the active channel_id is stored

### .env
This is where your bot token is stored

<br>

## Programme explaination

### setup.py -> get_id()
argument: None <br>
return: id -> string <br>
get_id() functions return the channel_id that is stored in the channel_id.txt

### setup.py -> set_id(message)
argument: message -> discord.Message <br>
return: status -> int <br>
set_id() function set the channel id to given argument. returns 1 if no argument is given, returns 2 if too much argument is given, return 0 if only 1 argument is given

### setup.py -> get_limit()
argument: None <br>
return: string -> 
get the current minimum word limit from limit.txt

### setup.py -> set_limit(message)
argument: message -> discord.Message
return: status -> int
set the limit to user defined and update the limit.txt according to it. returns the new limit that is set by the user. return -1, if there is no argument provided, return -2, if there is more than 2 argument provided, return -3, if the only argument is not an integer, return -4, if the only argument is an integer which is less than or equal to 0.

### story.py -> get_story(file)
argument: file -> string (name of the .txt file that stores the story) <br>
return: story -> string <br>
get_story() function compiles the story and count the word of the current story, if the word is strictly less than the current limit, it will prompt the user to input more words, otherwise, it will compile the story and print it to the text channel and empty the story.txt file and user.txt file

### story.py -> get_story_force(file)
argument: file -> string (name of the .txt file that stores the story) <br>
return: story -> string <br>
get_story_force() function compiles the story and send it the the server channel regardless of it's word counts, user needs admin permission to use this command

### story.py -> add_word(message, file)
argument: message -> discord.Message, file -> string (story.txt file) <br>
return: boolean <br>
add_word first check if the word is eligible meaning if the length of the message is at most 1 word, if not then it return false. Then it checks if the current user is same as the latest user  using user.txt who has added a word, if it is same, then it returns false. If the message has passed all the security check then the message is added to story.txt file in a single line and the user who sent the message will be appended user.txt file in a single line

### main.py
main.py maintains various commands and how the programme shall execute it


