from io import BytesIO
from discord.ext import commands
import discord
from PIL import Image


class Img(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def wanted(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author
        base = Image.open("assets/images/wanted_base.jpg")
        avatar = BytesIO(await user.avatar_url_as(size=128).read())
        avatar_image = Image.open(avatar)
        avatar_image = avatar_image.resize((126, 126))
        base.paste(avatar_image, (30, 94))
        base.save("temp/wanted.jpg")
        await ctx.send(file=discord.File("temp/wanted.jpg"))


def setup(client):
    client.add_cog(Img(client))
