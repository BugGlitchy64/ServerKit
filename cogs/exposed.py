import discord
from discord.ext import commands
import random

class exposed(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('exposed is OK!')
        
    @commands.command()
    async def thoughts(self, ctx):
        color = discord.Color(1242520)
        user = discord.User.display_name
        embed = discord.Embed(description = user + "fuck you!", color = color)
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(exposed(client))