import asyncio

import discord
from discord import client
from discord.ext import commands




class admin(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await ctx.message.delete(delay=0)
        await member.send(f"You was kicked from server")
        await ctx.send(f"Member {member.mention} was kicked from this server!")
        await member.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await ctx.send(f"Member {member.mention} was banned on this server")
        await member.ban(reason=reason)
        await ctx.message.delete(delay=0)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user_id: int):
        user = await client.fetch_user(user_id)
        await ctx.guild.unban(user)
        await ctx.message.delete(delay=0)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ping(self, ctx):
        await ctx.send("pong!")




async def setup(client):
    await client.add_cog(admin(client))