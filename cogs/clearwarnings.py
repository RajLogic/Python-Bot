import json
import discord
from discord.ext import commands
from discord import app_commands

# Load the warnings data from the JSON file or initialize a new one
report_data_path = 'data/reports.json'
try:
    with open(report_data_path, 'r', encoding='utf-8') as f:
        report = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    report = {'users': []}  # Initialize if the file doesn't exist or is invalid

class ClearWarnings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clearwarnings", help="Clears all warnings for a specified user.")
    @commands.has_permissions(administrator=True)
    async def clearwarnings(self, ctx, user: discord.User):
        """Clears all warnings for a specified user."""
        # Filter out warnings for the specified user
        initial_count = len(report['users'])
        report['users'] = [entry for entry in report['users'] if entry['user_id'] != user.id]

        # Save the updated warnings data back to the file
        with open(report_data_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=4)

        cleared_count = initial_count - len(report['users'])
        if cleared_count > 0:
            await ctx.send(f"Warnings cleared for {user.mention}.")
            try:
                await user.send("Your warnings have been cleared.")
            except discord.Forbidden:
                await ctx.send(f"Could not send a DM to {user.mention}.")
        else:
            await ctx.send(f"{user.mention} has no warnings to clear.")

    @clearwarnings.error
    async def clearwarnings_error(self, ctx, error):
        """Handles errors for the clearwarnings command."""
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to clear warnings.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify a user to clear warnings for.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Invalid user specified. Please mention a valid user.")
        else:
            await ctx.send("An unexpected error occurred.")
            raise error  # Re-raise for debugging

    @app_commands.command()
    async def clearwarnings(self, interaction: discord.Interaction, user: discord.User):
        """Clears all warnings for a specified user."""
        # Filter out warnings for the specified user
        initial_count = len(report['users'])
        report['users'] = [entry for entry in report['users'] if entry['user_id'] != user.id]

        # Save the updated warnings data back to the file
        with open(report_data_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=4)

        cleared_count = initial_count - len(report['users'])
        if cleared_count > 0:
            await interaction.response.send_message(f"Warnings cleared for {user.mention}.")
            try:
                await user.send("Your warnings have been cleared.")
            except discord.Forbidden:
                await interaction.response.send_message(f"Could not send a DM to {user.mention}.")
        else:
            await interaction.response.send_message(f"{user.mention} has no warnings to clear.")

    @clearwarnings.error
    async def clearwarnings_error(self, interaction: discord.Interaction, error):
        """Handles errors for the clearwarnings command."""
        if isinstance(error, commands.MissingPermissions):
            await interaction.response.send_message("You do not have permission to clear warnings.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await interaction.response.send_message("Please specify a user to clear warnings for.")
        elif isinstance(error, commands.BadArgument):
            await interaction.response.send_message("Invalid user specified. Please mention a valid user.")
        else:
            await interaction.response.send_message("An unexpected error occurred.")
            raise error  # Re-raise for debugging
        
async def setup(bot):
    """Asynchronous cog setup."""
    await bot.add_cog(ClearWarnings(bot))
