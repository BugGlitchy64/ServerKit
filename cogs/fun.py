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
import random

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("[DEBUG] Fun is OK!")
        
    @commands.command(
        name = 'thoughts', description = "Random thoughts and all.", usage = "Fun"
    )
    async def thoughts(self, ctx):
        thoughtlist = [
        'Man you got issues', 
        'Ok brain now shut up', 
        'Good Night and FUCK YOU!',
        'Bread',
        'Hamburger',
        'You are not funny'
        ]
        random.seed()
        embed = discord.Embed(title = "💭 Here's your thought", description = thoughtlist[random.randrange(0, len(thoughtlist))], color = self.client.color)
        await ctx.send(embed = embed, reference = ctx.message)

    @commands.command(
        name = 'eightball', description = "Ask and see what the 8ball tells you", usage = "Fun"
    )
    async def eightball(self, ctx):
        eightballList = [
        'Yes', 
        'No', 
        'Maybe',
        'Possibly Yes',
        'Possibly No',
        'In a million years, no',
        'In a million years, yes'
        ]
        random.seed()
        embed = discord.Embed(title = "🎱 8 ball answers:", description = eightballList[random.randrange(0, len(eightballList))], color = self.client.color)
        await ctx.send(embed = embed, reference = ctx.message)

    @commands.command(
        name = 'dice', description = "Roll a dice!", usage = "Fun"
    )
    async def dice(self, ctx, number):
        random.seed()
        embed = discord.Embed(title = "🎲 Dice rolls a/an...", description = f"{random.randint(1,int(number))}!", color = self.client.color)
        await ctx.send(embed = embed, reference = ctx.message)

def setup(client):
    client.add_cog(fun(client))