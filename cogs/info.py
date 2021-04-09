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

from dotenv import load_dotenv
load_dotenv()
import os
import discord
from discord.ext import commands

class info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("[DEBUG] Info is OK!")
        
    @commands.command(
        name = 'info', description = "Shows the info about the bot!", usage = "Information"
    )
    async def info(self, ctx):
        embed = discord.Embed(title = 'ServerKit', color = self.client.color)
        embed.description = "This is a bot that came from the fustration of some bot features are locked by subscription and servers with a lot of bots, simplicity should be in every server. Written by BugGlitchy64."
        embed.add_field(name = "Invite link", value = "https://discord.com/oauth2/authorize?client_id=828582617254461481&scope=bot&permissions=8")
        embed.add_field(name = "Github link", value = "https://github.com/BugGlitchy64/ServerKit")
        embed.set_footer(text = f"Version {self.client.version}")
        await ctx.send(embed = embed)


def setup(client):
    client.add_cog(info(client))