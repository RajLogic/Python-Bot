import discord
from imdb import Cinemagoer
import time 
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import  MissingPermissions,has_permissions
import json


load_dotenv('Bot-Python/data/.env')
token = os.getenv('DISCORD_TOKEN')
prefix = os.getenv('DISCORD_PREFIX')
link = os.getenv('DISCORD_LINK')
ownerid = os.getenv('DISCORD_OWNERID')

bot = discord.Bot(intents=discord.Intents.all(),)

@bot.event
async def on_ready():
    print("----------------------")
    print("Logged In As")
    print("Username: %s"%bot.user.name)
    print("ID: %s"%bot.user.id)
    print("----------------------")
    print(prefix)

@bot.slash_command(pass_context=True, name='setactivity')
async def setgame(ctx, *, activity1):
    """Sets my game (Owner)"""
    if ctx.author.id == (354879221044084737):
        message = ctx.message
        #await ctx.delete()
        await ctx.respond(f"Game was set to **{format(activity1)}**!")
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=activity1))


extensions = [# load cogs
    'cogs.ping',
    'cogs.hello',
    'cogs.botinvite',
    'cogs.serverinvite',
    'cogs.serverinfo',
    'cogs.movie',
    'cogs.help',
    #'cogs.gtn',  - need fixing
    'cogs.warn',
    'cogs.warnings',
    'cogs.clearwarnings',
    'cogs.kick',
    'cogs.ban',
    'cogs.unban',
   


]

if __name__ == '__main__': # import cogs from cogs folder
    for extension in extensions:
        bot.load_extension(extension)
bot.run(token)
