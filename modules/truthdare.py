from discord.ext import commands
import json
import random

with open("files/truth_dare.json") as data:
    data = json.load(data)
    verison = data["version"]
    truths = data["truths"]
    dares = data["dares"]
    print(f"Truths and Dares v: {verison}")


class TruthDare(commands.Cog):
    def __init__(self, client):
        self.client = client
        # TODO Load truths and dares from json file

    @commands.command()
    async def truth(self, ctx):
        # TODO get a random truth question from json file and send it
        await ctx.send("Truth Question")

    @commands.command()
    async def dare(self, ctx):
        # TODO get a random dare and send it
        await ctx.send("Dare 4 u")


def setup(client):
    client.add_cog(TruthDare(client))
