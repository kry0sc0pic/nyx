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

    @commands.command()
    async def jesus(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author
        base = Image.open("assets/images/jesus_base.jpg")
        avatar = BytesIO(await user.avatar_url_as(size=128).read())
        avatar_image = Image.open(avatar)
        avatar_image = avatar_image.resize((50, 50))
        base.paste(avatar_image, (64, 56))
        base.save("temp/jesus.jpg")
        await ctx.send(file=discord.File("temp/jesus.jpg"))

    
    @commands.command()
    async def trash(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author
        base = Image.open("assets/images/trash_base.png")
        avatar = BytesIO(await user.avatar_url_as(size=128).read())
        avatar_image = Image.open(avatar)
        avatar_image = avatar_image.resize((50, 50))
        base.paste(avatar_image, (23, 39))
        base.save("temp/trash.png")
        await ctx.send(file=discord.File("temp/trash.png"))
     
    @commands.command()
    async def laugh(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author
        base = Image.open("assets/images/laugh_base.jpg")
        avatar = BytesIO(await user.avatar_url_as(size=128).read())
        avatar_image = Image.open(avatar)
        avatar_image = avatar_image.resize((81, 81))
        base.paste(avatar_image, (41, 22))
        base.save("temp/laugh.jpg")
        await ctx.send(file=discord.File("temp/laugh.jpg"))
        
        
    @commands.command()
    async def award(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author
        base = Image.open("assets/images/award_base.jpg")
        avatar = BytesIO(await user.avatar_url_as(size=128).read())
        avatar_image = Image.open(avatar)
        avatar_image = avatar_image.resize((258, 258))
        base.paste(avatar_image, (657, 5))
        base.paste(avatar_image, (296, 128))
        base.save("temp/award.png")
        await ctx.send(file=discord.File("temp/award.png"))





def setup(client):
    client.add_cog(Img(client))
