import discord
from discord.ext import commands

class ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ping is OK!')
        
    @commands.command()
    async def ping(self, ctx):
        color = discord.Color(1242520)
        ping = str(round(self.client.latency * 1000))
        embed = discord.Embed(title = ':ping_pong: Pong!', description = '**' + ping + '**' + 'ms', color = color)
        await ctx.send(embed = embed)


def setup(client):
    client.add_cog(ping(client))