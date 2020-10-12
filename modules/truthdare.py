from discord.ext import commands


class TruthDare(commands.Cog):
    def __init__(self, client):
        self.client = client

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
