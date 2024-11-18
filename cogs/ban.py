import json
import discord
from discord.ext import commands
from discord import app_commands

# Load existing ban data or create a new one
ban_data_path = 'data/bans.json'
try:
    with open(ban_data_path, 'r', encoding='utf-8') as f:
        bans = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    bans = {'users': []}  # Initialize with an empty list if the file doesn't exist or is invalid


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ban")
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, user: discord.Member, *, reason: str = "No reason provided"):
        """Bans a user and logs the ban in a JSON file."""
        # Append ban details to the bans dictionary
        bans['users'].append({
            'username': user.name,
            'user_id': user.id,
            'reason': reason
        })

        # Save the updated bans data to the JSON file
        with open(ban_data_path, 'w', encoding='utf-8') as f:
            json.dump(bans, f, ensure_ascii=False, indent=4)

        # Notify the user and ban them
        try:
            await user.send(f"You have been banned from {ctx.guild.name} for the following reason: {reason}")
        except discord.Forbidden:
            await ctx.send(f"Could not DM {user.mention} about the ban.")
        
        await user.ban(reason=reason)
        await ctx.send(f"{user.mention} has been banned for the following reason: {reason}")

    @ban.error
    async def ban_error(self, ctx, error):
        """Handles errors for the ban command."""
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have the required permissions to use this command.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify both a user and a reason.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Could not find the specified user. Please ensure they are a member of this server.")
        else:
            await ctx.send("An unexpected error occurred.")
            raise error  # Re-raise the error for logging
        

    
    @app_commands.command()

    async def ban(self, interaction: discord.Interaction, user: discord.Member, reason: str = "No reason provided"):
        """Bans a user and logs the ban in a JSON file."""
        # Append ban details to the bans dictionary
        bans['users'].append({
            'username': user.name,
            'user_id': user.id,
            'reason': reason
        })
        
        # Save the updated bans data to the JSON file
        with open(ban_data_path, 'w', encoding='utf-8') as f:
            json.dump(bans, f, ensure_ascii=False, indent=4)

        # Notify the user and ban them
        try:
            await user.send(f"You have been banned from {interaction.guild.name} for the following reason: {reason}")
        except discord.Forbidden:
            await interaction.response.send_message(f"Could not DM {user.mention} about the ban.")

        await user.ban(reason=reason)
        await interaction.response.send_message(f"{user.mention} has been banned for the following reason: {reason}")

    @ban.error
    async def ban_error(self, interaction: discord.Interaction, error):
        """Handles errors for the ban command."""
        if isinstance(error, commands.MissingPermissions):
            await interaction.response.send_message("You do not have the required permissions to use this command.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await interaction.response.send_message("Please specify both a user and a reason.")
        elif isinstance(error, commands.BadArgument):
            await interaction.response.send_message("Could not find the specified user. Please ensure they are a member of this server.")
        else:
            await interaction.response.send_message("An unexpected error occurred.")
            raise error  # Re-raise the error for logging
async def setup(bot):
    """Asynchronous cog setup."""
    await bot.add_cog(Ban(bot))
