import discord
from discord.ext import commands
from discord import app_commands
import json

# Load the report data from the JSON file
with open('data/reports.json', encoding='utf-8') as f:
    try:
        report = json.load(f)
    except ValueError:
        report = {'users': []}

class Warnings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="warnings")
    @commands.has_permissions(administrator=True)
    async def warnings(self, interaction: discord.Interaction, user: discord.User):
        user_warnings = [entry for entry in report['users'] if entry['user_id'] == user.id]
        num_warnings = len(user_warnings)
        await interaction.response.send_message(f"{user.mention} has {num_warnings} warnings.")

    @warnings.error
    async def warnings_error(self, interaction: discord.Interaction, error):
        if isinstance(error, commands.MissingPermissions):
            await interaction.response.send_message("You can't do that!")

async def setup(bot):
    await bot.add_cog(Warnings(bot))
