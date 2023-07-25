
import discord
from discord import client
from discord.ext import commands




class General(commands.Cog):

    def __init__(self, client):
        self.client = client



async def setup(client):
    await client.add_cog(General(client))