import discord
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, client)
        self.client = client
        self.bot = bot
        bot.remove_command('help')

    @commands.Cog.listener()
    async def on_ready(self):
        print('Help is OK!')
        
    @client.command()
    async def help(self, tx):
        color = discord.Color(1242520)
        embed = discord.Embed(title = 'Help', color = color)
        embed.add_field(name = 'help', value = 'Shows this help message!', inline = False)
        embed.add_field(name = 'ping', value = 'A ping command!', inline = False)


def setup(client):
    client.add_cog(help(client))