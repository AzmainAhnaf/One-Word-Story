# One Word Story Bot

## TL;DR
The program is a functional discord bot that creates story from words given by the users of the server

## Setting up the bot in your server
### Step 1: Making your own bot
Go to [Discord Developer Portal](https://www.discord.com/developers/applications) and create your own bot from their
if you are having trouble, you can watch this [Youtube video](https://www.youtube.com/watch?v=UYJDKSah-Ww)
from 2:24 to 6:30. Collect your token
### Step 2: Clone the repository
Clone this repository and inside the .env file, insert your bot token
### Step 3: Run your bot
Run your bot locally from your machine or use any cloud service that you are comfortable with

## Bot Commands Functionlity
### ?settextchannel \[text_channel_id\]
use ?settextchannel in the above mentioned way to set the text channel where the bot will collect words from and show the story it has compiled so far

### ?makestory
use ?makestory to compile the story from so far collected words. This function only works if the word limit has reached the minimum_limit

### ?forcemakestory
use ?forcemakestory to compile the story regardless of minimum world limit, this command can only work if you have administrator privilege in the server

### ?limit \[number\] -> In development process
change the minimum word limit of you bot
