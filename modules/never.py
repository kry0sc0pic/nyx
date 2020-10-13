from discord.ext import commands
import json
import random


with open("files/truth_dare.json") as data:
    data = json.load(data)
    nevers = data["nevers"]


class Never(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["n"])
    async def never(self, ctx):
        never = random.choice(nevers)
        await ctx.send(never)


def setup(client):
    client.add_cog(Never(client))
