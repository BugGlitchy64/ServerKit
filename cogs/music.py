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

import youtube_dl
import asyncio
import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option

ytdl_format_options = {
    'format': 'bestaudio/best',
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0', # bind to ipv4 since ipv6 addresses cause issues sometime
    'cachedir': False,
}

ffmpeg_options = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url']
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

class music(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("[DEBUG] Music is OK!")

    async def join(self, ctx, normalCommand):
        voice = ctx.guild.voice_client
        if voice and voice.is_connected():
            await voice.disconnect()
        else:
            connected = ctx.author.voice
            if connected:
                await connected.channel.connect()
            channel = ctx.author.voice.channel.name
        embed = discord.Embed(title = '➕ Joined channel!', description = f'Check `{channel}` if I joined!', color = self.client.color)
        if normalCommand:
            await ctx.send(embed = embed, reference = ctx.message)
        else:
            await ctx.send(embed = embed)

    async def leave(self, ctx, normalCommand):
        voice = ctx.guild.voice_client
        if voice and voice.is_connected():
            await voice.disconnect()
        embed = discord.Embed(title = '➖ Left Channel', description = "Let's jam later!", color = self.client.color)
        if normalCommand:
            await ctx.send(embed = embed, reference = ctx.message)
        else:
            await ctx.send(embed = embed)

    async def play(self, ctx, normalCommand, *search):
        voice = ctx.guild.voice_client
        searchList = list(search)
        if type(searchList[0]) == tuple:
            keyword = ' '.join(list(searchList[0]))
        else:
            keyword = ' '.join(searchList)
        if not voice or not voice.is_connected():
            embed = discord.Embed(title = '😕 Ayo??', description = 'Hello? Where are you? Connect to a channel and try again!', color = self.client.color)
        elif not searchList:
            embed = discord.Embed(title = '😕 No link/keyword', description = 'Are you dumb? No link/keyword = No music! Provide link and try again!', color = self.client.color)
        elif searchList and voice.is_playing() or voice.is_paused():
            embed = discord.Embed(title = '😔 Queue is not supported yet!', description = f'Queue function will be added in a future update. Please use {self.client.command_prefix}stop or wait for it to finish!', color = self.client.color)
        elif not voice.is_playing() and voice.is_paused() and link is None:
            voice.resume()
            embed = discord.Embed(title = '▶️ Resuming...', description = 'Music should be resumed now!', color = self.client.color)
        else:
            player = await YTDLSource.from_url(keyword, loop=None)
            voice.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
            embed = discord.Embed(title = '▶️ Now playing', description = f'{player.title}', color = self.client.color)
        wait(1)
        if normalCommand:
            await ctx.send(embed = embed, reference = ctx.message)
        else:
            await ctx.send(embed = embed)

    async def stop(self, ctx, normalCommand):
        voice = ctx.guild.voice_client
        if not voice or not voice.is_connected():
            embed = discord.Embed(title = '😕 Ayo??', description = 'Hello? Where are you? Connect to a channel and try again!', color = self.client.color)
        elif not voice.is_playing() and not voice.is_paused():
            embed = discord.Embed(title = "😕 Ayo there's no music!", description = "Why don't you play some music for the homies?", color = self.client.color)
        else:
            voice.stop()
            embed = discord.Embed(title = '⏹️ Successfully stopped playing music.', description = 'No more jam! :(', color = self.client.color)
        if normalCommand:
            await ctx.send(embed = embed, reference = ctx.message)
        else:
            await ctx.send(embed = embed)

    async def pause(self, ctx, normalCommand):
        voice = ctx.guild.voice_client
        if not voice or not voice.is_connected():
            embed = discord.Embed(title = '😕 Ayo??', description = 'Hello? Where are you? Connect to a channel and try again!', color = self.client.color)
        elif voice.is_paused() and not voice.is_playing():
            embed = discord.Embed(title = '😕 Music is paused bro', description = f'Use {self.client.command_prefix}play to resume!', color = self.client.color)
        elif not voice.is_paused() and not voice.is_playing():
            embed = discord.Embed(title = "😕 Ayo there's no music!", description = "Why don't you play some music for the homies?", color = self.client.color)
        else:
            voice.pause()
            embed = discord.Embed(title = '⏸️ Music Paused.', description = '*Record Pauses*', color = self.client.color)
        if normalCommand:
            await ctx.send(embed = embed, reference = ctx.message)
        else:
            await ctx.send(embed = embed)
        
    @commands.command(
        name = 'join', description = "Join a music channel", usage = "Music"
    )
    async def normalJoin(self, ctx):
        await self.join(ctx, True)

    @commands.command(
        name = 'leave', description = "leave a music channel", usage = "Music"
    )
    async def normalLeave(self, ctx):
        await self.leave(ctx, True)

    @commands.command(
        name = 'play', description = "Play a music from YouTube/Spotify", usage = "Music"
    )
    async def normalPlay(self, ctx, *search):
        await self.play(ctx, True, search)
        
    
    @commands.command(
        name = 'stop', description = "Stops music.", usage = "Music"
    )
    async def normalStop(self, ctx):
        await self.stop(ctx, True)

    @commands.command(
        name = 'pause', description = "Pauses music.", usage = "Music"
    )
    async def normalPause(self, ctx):
        await self.pause(ctx, True)

    @cog_ext.cog_slash(
        name = 'join', description = "Join a music channel"
    )
    async def slashJoin(self, ctx):
        await self.join(ctx, False)

    @cog_ext.cog_slash(
        name = 'leave', description = "leave a music channel"
    )
    async def slashLeave(self, ctx):
        await self.leave(ctx, False)

    @cog_ext.cog_slash(
        name = 'play', description = "Play a music from YouTube/Spotify",
        options=[
            create_option(
                 name="search",
                 description="Search term/Youtube link/Spotify link",
                 option_type=3,
                 required=True
               )
        ]
    )
    async def slashPlay(self, ctx, search):
        await self.play(ctx, False, search)

    @cog_ext.cog_slash(
        name = 'stop', description = "Stops music."
    )
    async def slashStop(self, ctx):
        await self.stop(ctx, False)

    @cog_ext.cog_slash(
        name = 'pause', description = "Pauses music."
    )
    async def slashPause(self, ctx):
        await self.pause(ctx, False)

def setup(client):
    client.add_cog(music(client))
