from discord.ext import commands
import json
import random

with open("files/truth_dare.json") as data:
    data = json.load(data)
    verison = data["version"]
    truths = data["truths"]
    dares = data["dares"]
    nevers = data["never"]
    print(f"Truths and Dares v: {verison}")


class TruthDare(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["t"])
    async def truth(self, ctx):
        truth = random.choice(truths)
        await ctx.send(truth)

    @commands.command(aliases=["d"])
    async def dare(self, ctx):
        dare = random.choice(dares)
        await ctx.send(dare)
    
    @commands.command(aliases=["n"])
    async def never(self, ctx):
        never = random.choice(nevers)
        await ctx.send(never)


def setup(client):
    client.add_cog(TruthDare(client))
