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

class mod(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("[DEBUG] Mod is OK!")
    
    @commands.command(
        name = 'kick', description = "Kicks a user.", usage = "Moderation"
    )
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        if user is None:
            embed = discord.Embed(title = '😕 No user', description = 'How can I kick someone if there is no user to kick? Mention someone and try again!', color = self.client.color)
            await ctx.send(embed = embed, reference = ctx.message)
        else:
            try:
                await user.kick(reason=reason)
                embed = discord.Embed(title = '🔨 Kicked', description = f'{user.name}#{user.discriminator} has kicked for `{reason}`', color = self.client.color)
                await ctx.send(embed = embed, reference = ctx.message)
                dm = await user.create_dm()
                embed = discord.Embed(title = "😔 You've been kicked", description = f'{ctx.author.name}#{ctx.author.discriminator} has kicked you for `{reason}`', color = self.client.color)
                await dm.send(embed = embed)
            except discord.Forbidden:
                embed = discord.Embed(title = "😕 Kick failed", description = f"Are they above you/the bot? Do you have the kick permission? Or you want to kick yourself? Try again!", color = self.client.color)
                await ctx.send(embed = embed, reference = ctx.message)
    
    @commands.command(
        name = 'ban', description = "Bans a user.", usage = "Moderation"
    )
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        if user is None:
            embed = discord.Embed(title = '😕 No user', description = 'How can I ban someone if there is no user to ban? Mention someone and try again!', color = self.client.color)
            await ctx.send(embed = embed, reference = ctx.message)
        else:
            try:
                await user.ban(delete_message_days=0, reason=reason)
                embed = discord.Embed(title = '🔨 Banned', description = f'{user.name}#{user.discriminator} has banned for `{reason}`', color = self.client.color)
                await ctx.send(embed = embed, reference = ctx.message)
                dm = await user.create_dm()
                embed = discord.Embed(title = "😔 You've been banned", description = f'{ctx.author.name}#{ctx.author.discriminator} has banned you for `{reason}`', color = self.client.color)
                await dm.send(embed = embed)
            except discord.Forbidden:
                embed = discord.Embed(title = "😕 Ban failed", description = f"Are they above you/the bot? Do you have the ban permission? Or you want to ban yourself? Try again!", color = self.client.color)
                await ctx.send(embed = embed, reference = ctx.message)

def setup(client):
    client.add_cog(mod(client))