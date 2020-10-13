from discord.ext import commands
import json
import random


with open("assets/json/questions.json") as data:
    data = json.load(data)
    truths = data["truths"]


class Truth(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["t"])
    async def truth(self, ctx):
        truth = random.choice(truths)
        await ctx.send(truth)


def setup(client):
    client.add_cog(Truth(client))
