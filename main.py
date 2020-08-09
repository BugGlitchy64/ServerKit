import discord
from discord.ext import commands
import webserver
from webserver import keep_alive
import os

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is Ready")

keep_alive()
TOKEN = os.environ.get("TOKEN")
client.run(TOKEN)
