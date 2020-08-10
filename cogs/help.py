import discord
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        bot.remove_command('help')

    @commands.Cog.listener()
    async def on_ready(self):
        print('Help is OK!')
        
    @commands.command()
    async def help(self, ctx):
        color = discord.Color(1242520)
        embed = discord.Embed(title = 'Help', color = color)
        embed.add_field(name = 'help', value = 'Shows this help message!', inline = False)
        embed.add_field(name = 'ping', value = 'A ping command!', inline = False)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(help(bot))