import discord
from discord.ext import commands
from discord import app_commands
import json
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Load report data
report_file_path = 'data/reports.json'
if not os.path.exists(report_file_path):
    os.makedirs(os.path.dirname(report_file_path), exist_ok=True)
    with open(report_file_path, 'w', encoding='utf-8') as f:
        json.dump({'users': []}, f)

with open(report_file_path, 'r', encoding='utf-8') as f:
    try:
        report = json.load(f)
    except ValueError:
        report = {'users': []}

class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="warn")
    @commands.has_permissions(administrator=True)
    async def warn(self, interaction: discord.Interaction, user: discord.User, reason: str):
        report['users'].append({
            'username': user.name,
            'user_id': user.id,
            'reason': reason
        })
        with open(report_file_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=4)
        await interaction.response.send_message(f"{user.mention} has been warned for {reason}.")
        await user.send(f"You have been warned for {reason}.")

    @warn.error
    async def warn_error(self, interaction: discord.Interaction, error):
        if isinstance(error, commands.MissingPermissions):
            await interaction.response.send_message("You can't do that!")

async def setup(bot):
    await bot.add_cog(Warn(bot))
