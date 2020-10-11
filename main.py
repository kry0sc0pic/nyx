import discord
from discord import activity
from discord.ext import commands
client = commands.Bot(command_prefix="!")
status = discord.Status.online
act = discord.Activity(type=discord.ActivityType.listening, name="to !help")


@client.event
async def on_ready():
    await client.change_presence(status=status, activity=act)
    print("Bot is Ready")

# client.run(token)
