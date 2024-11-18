import discord
from discord.ext import commands
from discord import app_commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clear", help="Clears a specified number of messages from the channel.")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, limit: int):
        """Clears a specified number of messages from the current channel."""
        if limit < 1:
            await ctx.send("You must specify a number greater than 0.")
            return

        await ctx.channel.purge(limit=limit + 1)  # Includes the command message
        await ctx.send(f"Cleared {limit} message(s) as requested by {ctx.author.mention}.")

    @clear.error
    async def clear_error(self, ctx, error):
        """Handles errors for the clear command."""
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have the required permissions to use this command.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify the number of messages to clear.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("The number of messages to clear must be a valid integer.")
        else:
            await ctx.send("An unexpected error occurred.")
            raise error  # Re-raise for logging and debugging purposes
        
    @app_commands.command()
    async def clear(self, interaction: discord.Interaction, limit: int):
        """Clears a specified number of messages from the channel."""
        if limit < 1:
            await interaction.response.send_message("You must specify a number greater than 0.")
            return

        await interaction.channel.purge(limit=limit + 1)  # Includes the command message
        await interaction.response.send_message(f"Cleared {limit} message(s) as requested by {interaction.user.mention}.")

    @clear.error
    async def clear_error(self, interaction: discord.Interaction, error):
        """Handles errors for the clear command."""
        if isinstance(error, commands.MissingPermissions):
            await interaction.response.send_message("You do not have the required permissions to use this command.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await interaction.response.send_message("Please specify the number of messages to clear.")
        elif isinstance(error, commands.BadArgument):
            await interaction.response.send_message("The number of messages to clear must be a valid integer.")
        else:
            await interaction.response.send_message("An unexpected error occurred.")
            raise error  # Re-raise for logging and debugging purposes
    

async def setup(bot):
    """Asynchronous cog setup."""
    await bot.add_cog(Clear(bot))
