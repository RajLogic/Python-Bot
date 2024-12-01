import discord
from discord.ext import commands
from discord import app_commands

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hello", help="Says hello!")
    async def hello(self, ctx):
        """A simple command to say hello."""
        await ctx.send("Hello! 👋")

    @app_commands.command()
    async def hello(self, interaction: discord.Interaction):
        """A simple command to say hello."""
        await interaction.response.send_message("Hello! 👋")
async def setup(bot):
    """Asynchronous cog setup."""
    await bot.add_cog(Hello(bot))
