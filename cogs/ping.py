import discord
from discord import app_commands
from discord.ext import commands
import time

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping', description='Returns bot latency.')
    async def ping(self, ctx):
        """Respond with the bot's latency."""
        print("Ping command invoked.")
        
        # Capture the start time
        start_time = time.time()
        
        # Send an initial message
        message = await ctx.send("Pinging...")
        
        # Calculate latency
        end_time = time.time()
        latency = (end_time - start_time) * 1000  # Convert to milliseconds
        
        # Edit the message to display the latency
        await message.edit(content=f":ping_pong: Pong! Latency: `{latency:.2f}ms`")

    @app_commands.command()
    async def ping(self, interaction: discord.Interaction):
        """Respond with the bot's latency."""
        print("Slash command invoked.")
        
        # Capture the start time
        start_time = time.time()
        
        # Send an initial message
        await interaction.response.send_message("Pinging...")
        
        # Calculate latency
        end_time = time.time()
        latency = (end_time - start_time) * 1000  # Convert to milliseconds
        
        # Edit the message to display the latency
        await interaction.edit_original_response(content=f":ping_pong: Pong! Latency: `{latency:.2f}ms`")

async def setup(bot):
    """Asynchronous cog setup."""
    await bot.add_cog(Ping(bot))