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
async def ping(ctx):
    ping = str(round(client.latency * 1000))
    embed = discord.Embed(title = ':ping_pong: Pong!', description = '**' + ping + '**' + 'ms', color = color)
    await ctx.send(embed = embed)

@client.command()
async def help(ctx):
    embed = discord.Embed(title = 'Help', color = color)
    embed.add_field(name = 'help', value = 'Shows this help message!', inline = False)
    embed.add_field(name = 'ping', value = 'A ping command!', inline = False)

keep_alive()
TOKEN = os.environ.get('TOKEN')
client.run(TOKEN)
