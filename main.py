import time
import discord
import config
from discord.ext import commands
import os
from discord import Button, SelectMenu, SelectOption, ButtonStyle


intents = discord.Intents.default()
intents.message_content = True




class MyBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix=config.prefix, intents=intents)

    async def setup_hook(self) -> None:
        ...


client = MyBot()
client.remove_command('help')




@client.event
async def on_ready():
    print(f'\n\nLogged in as : {client.user.name} - {client.user.id}\nVersion: {discord.__version__}\n')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name = 'Use {.help help} for help'))

@client.event
async def on_ready():
    await client.load_extension('cogs.admin')
    await client.load_extension('cogs.fun')
    await client.load_extension('cogs.music')
    await client.load_extension('cogs.main')
    await client.load_extension('cogs.leveling')

@client.command()
async def load(ctx, extensions):
    if ctx.author.id == 560112831371149312:
        await client.load_extension(f'cogs.{extensions}')
        await ctx.send("loaded")
    else:
        await ctx.send("no perms")



@client.command()
async def unload(ctx, extensions):
    if ctx.author.id == 560112831371149312:
        await client.unload_extension(f'cogs.{extensions}')
        await ctx.send("unloaded")
    else:
        await ctx.send("no perms")


@client.command()
async def reload(ctx, extensions):
    if ctx.author.id == 560112831371149312:
        await client.unload_extension(f'cogs.{extensions}')
        await client.load_extension(f'cogs.{extensions}')
        await ctx.send("reloaded")
    else:
        await ctx.send("no perms")



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        async def load():
            await client.load_extension(f'cogs.{filename[:-3]}')




client.run(config.token)