import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import logging
import asyncio

logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv('data/.env')

# Retrieve environment variables
token = os.getenv('DISCORD_TOKEN')
prefix = os.getenv('DISCORD_PREFIX')
link = os.getenv('DISCORD_LINK')
ownerid = int(os.getenv('DISCORD_OWNERID')) if os.getenv('DISCORD_OWNERID') else None

# Debug prints to verify environment variables
print(f"DISCORD_TOKEN: {token}")
print(f"DISCORD_PREFIX: {prefix}")
print(f"DISCORD_LINK: {link}")
print(f"DISCORD_OWNERID: {ownerid}")

# Check if the token is set
if not token:
    raise ValueError("DISCORD_TOKEN is not set in the .env file")

# Initialize the bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents, description="Discord Bot")

# Event: Bot Ready
@bot.event
async def on_ready():
    await bot.tree.sync()  # Sync app commands with Discord
    print("----------------------")
    print("Logged In As")
    print(f"Username: {bot.user.name}")
    print(f"ID: {bot.user.id}")
    print("----------------------")
    print(prefix)

@bot.command(name="sync") 
async def sync(ctx):
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s).")
    await ctx.send(f"Synced {len(synced)} command(s).")

# Command: Set Activity
@bot.command(name='setactivity')
async def setgame(ctx, *, activity1):
    """Sets the bot's activity (for the owner only)."""
    if ctx.author.id == ownerid:  # Use the owner ID from the .env file
        await ctx.message.delete()
        await ctx.send(f"Game was set to **{activity1}**!")
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity1))
    else:
        await ctx.send("You don't have permission to set the activity.")

# List of cogs to load
extensions = [
    'cogs.ban',
    'cogs.botinvite',
    'cogs.clear',
    'cogs.clearwarnings',
    'cogs.gtn',
    'cogs.hello',
    'cogs.help',
    'cogs.kick',
    'cogs.movie',
    'cogs.ping',
    'cogs.serverinfo',
    'cogs.serverinvite',
    'cogs.unban',
    'cogs.warn',
    'cogs.warnings',
    'cogs.userinfo',  
    'cogs.weather',
    'cogs.money'
]

# Load extensions
async def main():
    async with bot:
        for extension in extensions:
            try:
                await bot.load_extension(extension)
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                print(f"Failed to load extension '{extension}': {e}")

        # Start the bot
        await bot.start(token)

# Run the bot using asyncio.run
if __name__ == '__main__':
    asyncio.run(main())