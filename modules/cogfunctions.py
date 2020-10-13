from discord.ext import commands
from discord.ext.commands.core import ExtensionNotFound, ExtensionNotLoaded, ExtensionAlreadyLoaded


class CogFunctions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def disable(self, ctx, module):
        try:
            self.client.unload_extension("modules."+module.strip())
            await ctx.send(f"Disabled module: `{module}`")
        except ExtensionNotLoaded:
            await ctx.send(f"Module {module.strip()} is already disabled or doesn't exist")

    @commands.command()
    async def enable(self, ctx, module):
        try:
            self.client.load_extension("modules."+module.strip())
            await ctx.send(f"Enabled module: `{module.strip()}`")
        except ExtensionAlreadyLoaded:
            await ctx.send(f"Module {module.strip()} is already enabled")
        except ExtensionNotFound:
            await ctx.send(f"Module {module.strip()} doesn't exist")


def setup(client):
    client.add_cog(CogFunctions(client))
