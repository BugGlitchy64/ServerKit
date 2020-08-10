import discord
from discord.ext import commands
import webserver
from webserver import keep_alive
import os

client = commands.Bot(command_prefix = 'crt!')
color = 7CFC00

@client.event
async def on_ready():
    print("Bot is Ready")

@client.command()
async def ping(ctx):
    embed = discord.Embed(title = 'Pong!', description = str(**round(client.latency * 1000)**) + "ms", color = color)
    await ctx.send(embed = embed)

keep_alive()
TOKEN = os.environ.get("TOKEN")
client.run(TOKEN)
