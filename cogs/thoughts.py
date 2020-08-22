import discord
from discord.ext import commands
import random

class thoughts(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('thoughts is OK!')
        
    @commands.command()
    async def thoughts(self, ctx):
        thoughtlist = ['Bruh ossas', 'Meme tape', 'Good Night and FUCK YOU!']
        random.seed()
        color = discord.Color(1242520)
        embed = discord.Embed(title = ":thought_balloon: Here's your thought", description = thoughtlist[random.randrange(0, len(thoughtlist))], color = color)
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(thoughts(client))