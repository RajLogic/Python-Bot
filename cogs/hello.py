import discord
from discord.commands import slash_command
from discord.ext import commands

class hello(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @slash_command(name='hello',description='says hello')
    async def hello(
        self,
        ctx: discord.ApplicationContext
    ):
        await ctx.respond("Hello")
def setup(bot):
    bot.add_cog(hello(bot))
