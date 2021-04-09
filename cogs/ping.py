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

import discord
from discord.ext import commands

class ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("[DEBUG] Ping is OK!")
        
    @commands.command(
        name = 'ping', description = "Measure the delay between you and the bot!", usage = "Information"
    )
    async def ping(self, ctx):
        ping = str(round(self.client.latency * 1000))
        embed = discord.Embed(title = ':ping_pong: Pong!', description = '**' + ping + '**' + 'ms', color = self.client.color)
        await ctx.send(embed = embed)


def setup(client):
    client.add_cog(ping(client))