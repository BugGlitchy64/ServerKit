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

class info(commands.Cog):

    def __init__(self, client):
        self.client = client
        client.remove_command('help')

    @commands.Cog.listener()
    async def on_ready(self):
        print("[DEBUG] Info is OK!")
        
    @commands.command(
        name = 'info', description = "Shows the info about the bot!", usage = "Information"
    )
    async def info(self, ctx):
        embed = discord.Embed(title = 'ServerKit', color = self.client.color)
        embed.description = "This is a bot that came from the fustration of some bot features are locked by subscription and servers with a lot of bots, simplicity should be in every server. Written by BugGlitchy64."
        embed.add_field(name = "Invite link", value = "https://discord.com/api/oauth2/authorize?client_id=828582617254461481&permissions=2587094358&scope=bot%20applications.commands", inline=False)
        embed.add_field(name = "Github link", value = "https://github.com/BugGlitchy64/ServerKit", inline=False)
        embed.set_footer(text = f"Version {self.client.version}")
        await ctx.send(embed = embed, reference = ctx.message)

    @commands.command(
        name = 'help', aliases = ['commands'], description = "The help command lists all of the commands usable in the bot!", usage = "Information"
    )
    async def help(self, ctx, arg=None):
        cogs = [c for c in self.client.cogs.keys()]
        if arg == None:
            embed = discord.Embed(title = 'ℹ️ Important commands', color = self.client.color)
            embed.description = f'Here are a list of some important commands in the bot, prefix is `{self.client.command_prefix}`.\nType `{self.client.command_prefix}help (command)` for more info.\nType `{self.client.command_prefix}help 2` for miscellaneous commands.'
            embed.add_field(name = '🔨 Moderation', value = '`ban` `kick` `mute*` `warn*`', inline = True)
            embed.add_field(name = '🎵 Music', value = '`join` `play` `stop` `skip*` `voteskip*` `pause` `queue*`')
            embed.set_footer(text = 'You are in page 1/2. (* ones are in construction)')
        elif arg == "2":
            embed = discord.Embed(title = 'ℹ️ Miscellaneous commands', color = self.client.color)
            embed.description = f'Prefix is `{self.client.command_prefix}`.\nTo return to the important commands, type `{self.client.command_prefix}help`.'
            embed.add_field(name = 'ℹ️ Information', value = '`help` `info` `ping` `changelog`', inline = True)
            embed.add_field(name = '😂 Fun', value = '`eightball` `dice` `thoughts`', inline = True)
            embed.set_footer(text = 'You are in page 2/2. (* ones are in construction)')
        else:
            noCommand = True
            lowArg = arg.lower()
            for cog in cogs:
                for command in self.client.get_cog(cog).get_commands():
                    if lowArg == command.name:
                        embed = discord.Embed(title = f'{self.client.command_prefix}{command.name}', color = self.client.color)
                        embed.description = f'`{command.description}`'
                        embed.add_field(name = 'Category', value = command.usage, inline = True)
                        embed.add_field(name = 'Alias(es)', value = command.aliases, inline = True)
                        noCommand = False 
                        break
            if noCommand == True:    
                embed = discord.Embed(title = "Ayo this command doesn't exist!", color = self.client.color)
                embed.description = 'Did you made a typo, or are you curious as to if this command exists? Try again!'
        await ctx.send(embed = embed, reference = ctx.message)

    @commands.command(
        name = 'changelog', description = "Shows the version log about the bot!", usage = "Information"
    )
    async def changelog(self, ctx):
        embed = discord.Embed(title = 'Changelog', color = self.client.color)
        embed.description = "Version features and changes."
        embed.add_field(name = "Version 0.2.3", value = "Cleanup, final version before v0.3 (/shhhhh), and submit to top.gg, with few more features.", inline = False)
        embed.add_field(name = "Version 0.2.2", value = "New branding! (With cleanup)", inline = False)
        embed.add_field(name = "Version 0.2.1", value = "Major bug fixes!", inline = False)
        embed.add_field(name = "Version 0.2", value = "Added Music and changelog, with bug fixes!", inline = False)
        embed.add_field(name = "Version 0.1.1.4", value = "Bug fixes.", inline = False)
        embed.set_footer(text = f"Version {self.client.version}")
        await ctx.send(embed = embed, reference = ctx.message)

    @commands.command(
        name = 'ping', description = "Measure the delay between you and the bot!", usage = "Information"
    )
    async def ping(self, ctx):
        ping = str(round(self.client.latency * 1000))
        embed = discord.Embed(title = ':ping_pong: Pong!', description = '**' + ping + '**' + 'ms', color = self.client.color)
        await ctx.send(embed = embed, reference = ctx.message)

def setup(client):
    client.add_cog(info(client))