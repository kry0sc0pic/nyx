import discord
import json
import os
from discord.ext import commands
# from dotenv import load_dotenv  # for local testing
# load_dotenv()  # for local testing
client = commands.Bot(command_prefix="$")
status = discord.Status.online
act = discord.Activity(type=discord.ActivityType.listening, name="to $help")
with open("config/config.json") as jsonconfig:
    config = json.load(jsonconfig)


@client.event
async def on_ready():
    await client.change_presence(status=status, activity=act)
    print("Bot is Ready")
client.remove_command("help")

for cog in config["extensions"]:

    client.load_extension(cog)


token = os.environ.get("TOKEN")

try:
    client.run(token)
finally:
    temp_files = os.listdir("./temp")
    temp_files.remove(".nyx")
    for file in temp_files:
        os.remove(os.path.join("./temp", file))
        print("Deleted ./temp/"+file)
