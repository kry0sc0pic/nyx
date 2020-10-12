import discord
import json
import os
from discord.ext import commands
client = commands.Bot(command_prefix="$")
status = discord.Status.online
act = discord.Activity(type=discord.ActivityType.listening, name="to !help")
with open("config/config.json") as jsonconfig:
    config = json.load(jsonconfig)


@client.event
async def on_ready():
    await client.change_presence(status=status, activity=act)
    print("Bot is Ready")


for cog in config["load_cogs"]:

    client.load_extension(cog)


# token = "<token>" # For local testing
# token = os.environ.get("TOKEN") # For heroku deployment
