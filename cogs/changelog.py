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

class changelog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("[DEBUG] Changelog is OK!")
        
    @commands.command(
        name = 'changelog', description = "Shows the version log about the bot!", usage = "Information"
    )
    async def changelog(self, ctx):
        embed = discord.Embed(title = 'Changelog', color = self.client.color)
        embed.description = "Version features and changes."
        embed.add_field(name = "Version 0.2.2", value = "New branding! (With cleanup)", inline = False)
        embed.add_field(name = "Version 0.2.1", value = "Major bug fixes!", inline = False)
        embed.add_field(name = "Version 0.2", value = "Added Music and changelog, with bug fixes!", inline = False)
        embed.add_field(name = "Version 0.1.1.4", value = "Bug fixes.", inline = False)
        embed.set_footer(text = f"Version {self.client.version}")
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(changelog(client))