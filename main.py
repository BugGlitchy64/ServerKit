import discord
from discord.ext import commands
import webserver
from webserver import keep_alive
import os

client = commands.Bot(command_prefix = 'crt!')
color = discord.Color(1242520)


client.remove_command('help')


@client.event
async def on_ready():
    print("Bot is Ready")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
async def help(ctx):
    embed = discord.Embed(title = 'Help', color = color)
    embed.add_field(name = 'help', value = 'Shows this help message!', inline = False)
    embed.add_field(name = 'ping', value = 'A ping command!', inline = False)

keep_alive()
TOKEN = os.environ.get('TOKEN')
client.run(TOKEN)
