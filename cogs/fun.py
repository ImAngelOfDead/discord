import requests
import io
import json
import urllib.request
from bs4 import BeautifulSoup
import discord
import requests
from discord.ext import commands
import asyncio
import lxml

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.command()
    async def reply(self, ctx):
        await ctx.reply('reply', mention_author=True)


    @commands.command()
    async def facepalm(self, ctx):
        response = requests.get('https://some-random-api.ml/animu/face-palm')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xff9900, title='Facepalm')
        embed.set_image(url=json_data['link'])
        await ctx.send(embed=embed)

    @commands.command()
    async def wink(self, ctx):
        response = requests.get('https://some-random-api.ml/animu/wink')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xff9900, title='Random Wink')
        embed.set_image(url=json_data['link'])
        await ctx.send(embed=embed)

    @commands.command()
    async def virus(self, ctx, virus=None, *, user: discord.Member = None):
        virus = virus or 'discord'
        user = user or ctx.author
        with open('data/virus.txt') as f:
            animation = f.read().splitlines()
        base = await ctx.send(animation[0])
        for line in animation[1:]:
            await base.edit(content=line.format(virus=virus, user=user))
            await asyncio.sleep(1)




async def setup(client):
    await client.add_cog(fun(client))