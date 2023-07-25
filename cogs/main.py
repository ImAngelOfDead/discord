import datetime
import discord
from discord import client
from discord.ext import commands
from collections import OrderedDict, deque, Counter


EmbedColor = 0x4d004d

class main(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.command()
    async def help(self, ctx, arg):
        if arg == "admin":
            await ctx.send(embed=discord.Embed(
                description='**Admin commands:**\nPing\nBan\nKick\nUnban\nLoad\nUnload\nReload\nUse .help {command} to help on the command',
                colour=discord.Color.purple()))
        if arg == "fun":
            await ctx.send(
                embed=discord.Embed(description=f'**Fun commands:**\nReply\nWink\nFacepalm\nVirus', colour=discord.Color.purple()))
        if arg == "music":
            await ctx.send(embed=discord.Embed(description=f'**Music commands:**\nJoin\nStop\nYt\nVolume\n',
                                               colour=discord.Color.purple()))
        if arg == "help":
            await ctx.send(embed=discord.Embed(description=f'**Use one is this arguments:**\nAdmin\nFun\nMusic\nMain',
                                               colour=discord.Color.purple()))
        if arg == "main":
            await ctx.send(embed=discord.Embed(description=f'**Main commands:**\nhelp\ncoglist\n'))

        if arg == "ping":
            await ctx.send(
                embed=discord.Embed(description=f'**Ping - test bot ping status**\n', colour=discord.Color.purple()))
        if arg == "ban":
            await ctx.send(embed=discord.Embed(description=f'**Ban - user on this server**\nUsage - .ban @user',
                                               colour=discord.Color.purple()))
        if arg == "kick":
            await ctx.send(
                embed=discord.Embed(description=f'**Kick - kick user from this server**\nUsage - .kick @user',
                                    colour=discord.Color.purple()))
        if arg == "unban":
            await ctx.send(
                embed=discord.Embed(description='**Unban - unban user on this server**\nUsage - .unban {user id}',
                                    colour=discord.Color.purple()))
        if arg == "load":
            await ctx.send(embed=discord.Embed(description='**Load - load cog**\nUsage - .load {cog file name}',
                                               colour=discord.Color.purple()))
        if arg == "unload":
            await ctx.send(embed=discord.Embed(description='**Unload - unload cog**\nUsage - .unload {cog file name}',
                                               colour=discord.Color.purple()))
        if arg == "reload":
            await ctx.send(embed=discord.Embed(description='**Reload - reload cog**\nUsage - .reload {cog file name}',
                                               colour=discord.Color.purple()))
        if arg == "reply":
            await ctx.send(embed=discord.Embed(description='**Reply - bot reply on you message**\n',
                                               colour=discord.Color.purple()))
        if arg == "join":
            await ctx.send(embed=discord.Embed(description='**Join - bot connect to you voice channel**\n',
                                               colour=discord.Color.purple()))
        if arg == "stop":
            await ctx.send(
                embed=discord.Embed(description='**Stop - stop playing music**\n', colour=discord.Color.purple()))
        if arg == "yt":
            await ctx.send(embed=discord.Embed(description='**Yt - playing music on youtube link**\nUsage - .yt {link}',
                                               colour=discord.Color.purple()))
        if arg == "volume":
            await ctx.send(
                embed=discord.Embed(description='**Volume - set bot volume to value**\nUsage - .volume {volume}',
                                    colour=discord.Color.purple()))
        if arg == "coglist":
            await ctx.send(embed=discord.Embed(description='**Coglist - display cogs list**'))
        if arg == "rank":
            await ctx.send(embed=discord.Embed(description='**Rank - display you level and exp**'))
        if arg == "info":
            await ctx.send(embed=discord.Embed(description='**Info - display the bot info**'))
        if arg == "wink":
            await ctx.send(embed=discord.Embed(description='**Wink - send wink gif**'))
        if arg == "facepalm":
            await ctx.send(embed=discord.Embed(description='**Facepalm - send facepalm gif**'))
        if arg == "virus":
            await ctx.send(embed=discord.Embed(description='**Virus - send virus to you enemy**'))



    @commands.command()
    async def coglist(self, ctx):
        await ctx.send(embed=discord.Embed(description='**Its a cog list!**\nadmin\nfun\nmain\nmusic\nleveling'))




async def setup(client):
    await client.add_cog(main(client))