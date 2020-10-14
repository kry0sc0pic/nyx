from discord import colour
from discord import embeds
from discord.ext import commands
import discord


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        helpEmbed = discord.Embed(
            title="Bot Help", description="Help for Nyx Bot", colour=0xee6f57)
        helpEmbed.add_field(
            name="$help", value="Displays the help for the bot", inline=False)
        helpEmbed.add_field(
            name="$truth or $t", value="Sends a random truth question")
        helpEmbed.add_field(
            name="$dare or $d", value="Sends a random dare")
        helpEmbed.add_field(
            name="$never or $n", value="Sends a never have I ever question")
        helpEmbed.add_field(
            name="$wanted", value="Puts you avatar on a wanted poster", inline=False)
        helpEmbed.add_field(name="Github Repo",
                            value="https://github.com/krishaayjois21/nyx", inline=False)
        helpEmbed.set_thumbnail(url="https://i.imgur.com/fCZVySr.png")

        helpEmbed.set_footer(
            text="Like the bot? , Consider giving it a star on github 🙂")
        await ctx.send(embed=helpEmbed)


def setup(client):
    client.add_cog(Help(client))
