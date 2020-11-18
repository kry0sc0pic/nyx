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
    async def suggest(ctx , * , suggestion: str):
        embed = discord.Embed(title="Suggestion",
        description=f"Suggested By: {ctx.author.mention}",
        color=0xFFC83D
        )
        embed.add_field(name="Content" , value=suggestion)
        embed.set_thumbnail(url=ctx.author.avatar_url_as(size=128))
        embed.set_footer("Suggestions powered by Nyx")
        suggested = await ctx.send(embed=embed)
        await self.client.add_reaction(suggested , emoji=up)
        await self.client.add_reaction(suggested , emoji=down)
    
def setup(client):
    client.add_cog(Suggestions(client))
        