from discord.ext import commands
import json
import random


with open("files/truth_dare.json") as data:
    data = json.load(data)
    dares = data["dares"]


class Dare(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["d"])
    async def dare(self, ctx):
        dare = random.choice(dares)
        await ctx.send(dare)


def setup(client):
    client.add_cog(Dare(client))
