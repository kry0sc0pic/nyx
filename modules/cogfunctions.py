from discord.ext import commands
from discord.ext.commands.core import command


class CogFunctions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def disable(self, ctx, module):
        self.client.unload_extension("modules."+module.strip())
        await ctx.send(f"Disabled module: `{module}`")

    @commands.command()
    async def enable(self, ctx, module):
        self.client.load_extension("modules."+module.strip())
        await ctx.send(f"Enabled module: `{module.strip()}`")

    @commands.command()
    async def renable(self, ctx, module):
        self.client.unload_extension("modules."+module.strip())
        self.client.load_extension("modules."+module.strip())
        await ctx.send(f"Renabled module: `{module.strip()}`")


def setup(client):
    client.add_cog(CogFunctions(client))
