from discord import colour
from discord import embeds
from discord.ext import commands
import discord
import json

with open("assets/json/help.json", "r") as f:
    helpdata = json.load(f)
    thumb = helpdata["thumbnail"]
    helpdata = helpdata["data"]


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        helpEmbed = discord.Embed(
            title="Bot Help", description="Help for Nyx Bot", colour=0xee6f57)
        for field in helpdata:
            helpEmbed.add_field(
                name=field["name"], value=field["value"], inline=field["inline"])
        helpEmbed.set_thumbnail(url=thumb)

        helpEmbed.set_footer(
            text="Like the bot? , Consider giving it a star on github 🙂")
        await ctx.send(embed=helpEmbed)


def setup(client):
    client.add_cog(Help(client))
