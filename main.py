import discord
from discord.ext import commands
import webserver
from webserver import keep_alive
import os

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is Ready")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

keep_alive()
TOKEN = os.environ.get("TOKEN")
client.run(TOKEN)
