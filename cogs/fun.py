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
from discord_slash import cog_ext

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("[DEBUG] Fun is OK!")

    async def thoughts(self, ctx, normalCommand):
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
        if normalCommand:
            await ctx.send(embed = embed, reference = ctx.message)
        else:
            await ctx.send(embed = embed)

    async def eightball(self, ctx, normalCommand):
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
        if normalCommand:
            await ctx.send(embed = embed, reference = ctx.message)
        else:
            await ctx.send(embed = embed)

    async def dice(self, ctx, number, normalCommand):
        random.seed()
        embed = discord.Embed(title = "🎲 Dice rolls a/an...", description = f"{random.randint(1,int(number))}!", color = self.client.color)
        if normalCommand:
            await ctx.send(embed = embed, reference = ctx.message)
        else:
            await ctx.send(embed = embed)

    async def someone(self, ctx, normalCommand, *message):
        members = ctx.guild.members
        if type(message[0]) == tuple:
            strMessage = ' '.join(list(message[0]))
        else:
            strMessage = ' '.join(message)
        random.seed()
        while True:
            member = members[random.randrange(0, len(members))]
            if not member.bot and member.id != ctx.author.id:
                mentionUser = member
                break
        embed = discord.Embed(description = f"{strMessage}", color = self.client.color)
        if normalCommand:
            await ctx.send(content = mentionUser.mention, embed = embed, reference = ctx.message)
        else:
            await ctx.send(content = mentionUser.mention, embed = embed)
        
    @commands.command(
        name = 'thoughts', description = "Random thoughts and all.", usage = "Fun"
    )
    async def normalThoughts(self, ctx):
        await self.thoughts(ctx, True)

    @commands.command(
        name = 'eightball', description = "Ask and see what the 8ball tells you", usage = "Fun"
    )
    async def normalEightball(self, ctx):
        await self.eightball(ctx, True)

    @commands.command(
        name = 'dice', description = "Roll a dice!", usage = "Fun"
    )
    async def normalDice(self, ctx, number):
        await self.dice(ctx, number, True)

    @commands.command(
        name = 'someone', description = "Discord's April Fools feature, pings a random person.", usage = "Fun"
    )
    async def normalSomeone(self, ctx, *message):
        await self.someone(ctx, True, message)

    @cog_ext.cog_slash(
        name = 'thoughts', description = "Random thoughts and all."
    )
    async def slashThoughts(self, ctx):
        await self.thoughts(ctx, False)

    @cog_ext.cog_slash(
        name = 'eightball', description = "Ask and see what the 8ball tells you"
    )
    async def slashEightball(self, ctx):
        await self.eightball(ctx, False)

    @cog_ext.cog_slash(
        name = 'dice', description = "Roll a dice!"
    )
    async def slashDice(self, ctx, number):
        await self.dice(ctx, number, False)

    @cog_ext.cog_slash(
        name = 'someone', description = "Discord's April Fools feature, pings a random person."
    )
    async def slashSomeone(self, ctx, *message):
        await self.dice(ctx, False, message)

def setup(client):
    client.add_cog(fun(client))