from discord import channel
from discord.ext import commands
import discord
import json

up = "👍"
down = "👎"

with open("config/config.json") as conf:
    config = json.load(conf)
    channel_id = config["suggestions_channel"]


class Suggestions(commands.Cog):
    def __init__(self , client):
        self.client = client

    @commands.command()
    async def suggest(self , ctx , * , suggestion: str):
        embed = discord.Embed(title="Suggestion",
        description=f"Suggested By: {ctx.author.mention}",
        color=0xee6f57
        )
        embed.add_field(name="Content" , value=suggestion)
        embed.set_thumbnail(url=ctx.author.avatar_url_as(size=128))
        channel = self.client.get_channel(channel_id)
        suggested = await channel.send(embed=embed)
        await suggested.add_reaction(emoji=up)
        await suggested.add_reaction(emoji=down)
    
def setup(client):
    client.add_cog(Suggestions(client))
        