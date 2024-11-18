import discord
import os
from discord.ext import commands
from discord import app_commands

# Load the bot invite link from environment variables
link = os.getenv('DISCORD_LINK')

class BotInvite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="botinvite")
    async def botinvite(self, ctx):
        """Sends the bot invite link to the user's DM."""
        if not link:
            await ctx.send("Bot invite link is not set. Please configure it in the environment variables.")
            return

        try:
            await ctx.author.send(f"Here is the invite link for the bot: {link}")
            await ctx.send("Check your DMs for the bot invite link!")
        except discord.Forbidden:
            await ctx.send("I couldn't send you a DM. Please check your DM settings and try again.")

    @botinvite.error
    async def botinvite_error(self, ctx, error):
        """Handles errors for the botinvite command."""
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("An error occurred while trying to send you the bot invite link.")
        else:
            await ctx.send("An unexpected error occurred.")
            raise error  # Re-raise the error for logging
        
    @app_commands.command(name="botinvite")
    async def botinvite(self, interaction: discord.Interaction):
        """Sends the bot invite link to the user's DM."""
        if not link:
            await interaction.response.send_message("Bot invite link is not set. Please configure it in the environment variables.")
            return

        try:
            await interaction.response.send_message(f"Here is the invite link for the bot: {link}")
        except discord.Forbidden:
            await interaction.response.send_message("I couldn't send you a DM. Please check your DM settings and try again.")

    @botinvite.error
    async def botinvite_error(self, interaction: discord.Interaction, error):
        """Handles errors for the botinvite command."""
        if isinstance(error, commands.CommandInvokeError):
            await interaction.response.send_message("An error occurred while trying to send you the bot invite link.")
        else:
            await interaction.response.send_message("An unexpected error occurred.")
            raise error  # Re-raise the error for logging
async def setup(bot):
    """Asynchronous cog setup."""
    await bot.add_cog(BotInvite(bot))
