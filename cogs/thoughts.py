import discord
from discord.ext import commands
import random

class thoughts(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Help is OK!')
        
    @commands.command()
    thoughts = ['Bruh ossas', 'Meme tape']
    async def help(self, ctx):
        random.seed()
        color = discord.Color(1242520)
        embed = discord.Embed(title = ":thought_balloon: Here's your thought", description = thoughts[random.randrange(0,1)] ,color = color)
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(thoughts(client))