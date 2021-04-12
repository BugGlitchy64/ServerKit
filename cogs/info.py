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
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option

class info(commands.Cog):

    def __init__(self, client):
        self.client = client
        client.remove_command('help')

    @commands.Cog.listener()
    async def on_ready(self):
        print("[DEBUG] Info is OK!")

    async def info(self, ctx, normalCommand):
        embed = discord.Embed(title = 'ServerKit', color = self.client.color)
        embed.description = f"This command has been moved to {self.client.command_prefix}help"
        if normalCommand:
            await ctx.send(embed = embed, reference = ctx.message)
        else:
            await ctx.send(embed = embed)

    async def help(self, ctx, normalCommand, arg=None):
        cogs = [c for c in self.client.cogs.keys()]
        if arg == None:
            embed = discord.Embed(title = 'ℹ️ Important commands', color = self.client.color)
            embed.description = f'Here are a list of some important commands in the bot, prefix are `{self.client.command_prefix}` and `/`.\nType `{self.client.command_prefix}help (command)` for more info.\nType `{self.client.command_prefix}help 2` for miscellaneous commands.'
            embed.add_field(name = '🔨 Moderation', value = '`ban` `kick` `mute*` `warn*`', inline = True)
            embed.add_field(name = '🎵 Music', value = '`join` `play` `stop` `skip*` `voteskip*` `pause` `queue*`', inline = True)
            embed.add_field(name = 'Links', value = '[Support Server](https://discord.gg/YA5pTheC3A) [Invite link](https://discord.com/api/oauth2/authorize?client_id=828582617254461481&permissions=2587094358&scope=bot%20applications.commands) [Github](https://github.com/BugGlitchy64/ServerKit)', inline = False)
            embed.set_footer(text = 'You are in page 1/2. (* ones are in construction)')
        elif arg == "2":
            embed = discord.Embed(title = 'ℹ️ Miscellaneous commands', color = self.client.color)
            embed.description = f'Prefix are `{self.client.command_prefix}` or `/`.\nTo return to the important commands, type `{self.client.command_prefix}help`.'
            embed.add_field(name = 'ℹ️ Information', value = '`help` `info` `ping` `changelog`', inline = True)
            embed.add_field(name = '😂 Fun', value = '`eightball` `dice` `thoughts` `someone`', inline = True)
            embed.add_field(name = 'Links', value = '[Support Server](https://discord.gg/YA5pTheC3A) [Invite link](https://discord.com/api/oauth2/authorize?client_id=828582617254461481&permissions=2587094358&scope=bot%20applications.commands) [Github](https://github.com/BugGlitchy64/ServerKit)', inline = False)
            embed.set_footer(text = 'You are in page 2/2. (* ones are in construction)')
        else:
            noCommand = True
            lowArg = arg.lower()
            for cog in cogs:
                for command in self.client.get_cog(cog).walk_commands():
                    if lowArg == command.name:
                        embed = discord.Embed(title = f'{self.client.command_prefix}{command.name} (or /{command.name})', color = self.client.color)
                        embed.description = f'`{command.description}`'
                        embed.add_field(name = 'Category', value = command.usage, inline = True)
                        embed.add_field(name = 'Alias(es)', value = command.aliases, inline = True)
                        noCommand = False 
                        break
            if noCommand == True:    
                embed = discord.Embed(title = "Ayo this command doesn't exist!", color = self.client.color)
                embed.description = 'Did you made a typo, or are you curious as to if this command exists? Try again!'
        if normalCommand:
            await ctx.send(embed = embed, reference = ctx.message)
        else:
            await ctx.send(embed = embed)

    async def changelog(self, ctx, normalCommand):
        embed = discord.Embed(title = 'Changelog', color = self.client.color)
        embed.description = "This command has been moved to [Github](https://github.com/BugGlitchy64/ServerKit/blob/master/CHANGELOG.md)"
        if normalCommand:
            await ctx.send(embed = embed, reference = ctx.message)
        else:
            await ctx.send(embed = embed)

    async def ping(self, ctx, normalCommand):
        ping = str(round(self.client.latency * 1000))
        embed = discord.Embed(title = ':ping_pong: Pong!', description = '**' + ping + '**' + 'ms', color = self.client.color)
        if normalCommand:
            await ctx.send(embed = embed, reference = ctx.message)
        else:
            await ctx.send(embed = embed)
        
    @commands.command(
        name = 'info', description = "Shows the info about the bot!", usage = "Information"
    )
    async def normalInfo(self, ctx):
        await self.info(ctx, True)

    @commands.command(
        name = 'help', aliases = ['commands'], description = "The help command lists all of the commands usable in the bot!", usage = "Information"
    )
    async def normalHelp(self, ctx, arg=None):
        await self.help(ctx, True, arg)

    @commands.command(
        name = 'changelog', description = "Shows the version log about the bot!", usage = "Information"
    )
    async def normalChangelog(self, ctx):
        await self.changelog(ctx, True)

    @commands.command(
        name = 'ping', description = "Measure the delay between you and the bot!", usage = "Information"
    )
    async def normalPing(self, ctx):
        await self.ping(ctx, True)

    @cog_ext.cog_slash(
        name = 'info', description = "Shows the info about the bot!"
    )
    async def slashInfo(self, ctx):
        await self.info(ctx, False)

    @cog_ext.cog_slash(
        name = 'help', description = "The help command lists all of the commands usable in the bot!",
        options=[
            create_option(
                 name="command",
                 description="Insert a command to see descriptions and other info.",
                 option_type=3,
                 required=False
               )
        ]
    )
    async def slashHelp(self, ctx, arg=None):
        await self.help(ctx, False, arg)

    @cog_ext.cog_slash(
        name = 'changelog', description = "Shows the version log about the bot!"
    )
    async def slashChangelog(self, ctx):
        await self.changelog(ctx, False)

    @cog_ext.cog_slash(
        name = 'ping', description = "Measure the delay between you and the bot!"
    )
    async def slashPing(self, ctx):
        await self.ping(ctx, False)

def setup(client):
    client.add_cog(info(client))