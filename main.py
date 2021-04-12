# Copyright (C) 2021 BugGlitchy64
# 
# This file is part of ServerKit.
# 
# ServerKit is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# ServerKit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with ServerKit.  If not, see <http://www.gnu.org/licenses/>.

import asyncio
from dotenv import load_dotenv
load_dotenv()
import os
import discord
from discord.ext import commands
from discord_slash import SlashCommand

if os.getenv("PRODUCTION") == "True":
    client = commands.Bot(command_prefix = 'server.', case_insensitive = True, intents=discord.Intents.all())
else:
    client = commands.Bot(command_prefix = 'serverd.', case_insensitive = True, intents=discord.Intents.all())

slash = SlashCommand(client, override_type = True, sync_commands=True, sync_on_cog_reload=True)

if os.getenv("PRODUCTION") == "True":
    client.color = 0x7289da
else:
    client.color = 0xffb600

if os.getenv("PRODUCTION") == "True":
    client.version = "Alpha 0.3.5.1"
else:
    client.version = "Alpha-DEV 0.4"

async def status_task():
    while True:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{client.command_prefix}help and /help"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name=f"at version {client.version}"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers!"))
        await asyncio.sleep(10) 

@client.event
async def on_ready():
    print("=== ServerKit ===")
    if os.getenv("PRODUCTION") == "False":
        print("Bot is now running in development mode, with development cogs, please throughly check for errors!")
    print("Bot is now running cogs (commands)... Please check for potential errors or debug messages.")
    client.loop.create_task(status_task())

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    if os.getenv("PRODUCTION") == "False":
        client.load_extension(f'cogs.{extension}')
        embed = discord.Embed(color = client.color)
        embed.description = f'`{extension}` loaded!'
        await ctx.send(embed = embed)

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    if os.getenv("PRODUCTION") == "False":
        client.unload_extension(f'cogs.{extension}')
        embed = discord.Embed(color = client.color)
        embed.description = f'`{extension}` unloaded!'
        await ctx.send(embed = embed)

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    if os.getenv("PRODUCTION") == "False":
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        embed = discord.Embed(color = client.color)
        embed.description = f'`{extension}` reloaded!'
        await ctx.send(embed = embed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

if os.getenv("PRODUCTION") == "True":
    client.run(os.getenv("PRODUCTIONTOKEN"))
else:
    client.run(os.getenv("DEVTOKEN"))
