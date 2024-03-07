import random
import discord
from imdb import Cinemagoer
import time
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.commands import slash_command
from discord.ext.commands import Bot
from discord.ext.commands import  MissingPermissions,has_permissions
import json

class help(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @slash_command(description = "help")
    async def help(
        self,
        ctx: discord.ApplicationContext
    ):
        help_text = """
     General Commands: `all in slash`
    - `help`: Shows this help message
    - `ping`: Shows the bot's latency
    - `serverinvite` : Sends an invite link to our Server
    - `movie <movie name>` : Shows information about a movie
    - `gtn`: Plays a Guess-the-Number game
    - `hello`: Says hello
    - `botinvite`: Sends a link to invite the bot to your server
    - `serverinfo`: Shows information about the server

    
    Moderation Commands (Requires Manage Server Permission):
    Admin Commands: `all in slash`
    - `clear <number>`: Clears a number of messages from the channel
    - `purge <number>`: Purges a number of messages from the channel
    - `purge` : clears chat
    - `setactivity <activity>`: Sets the bot's activity (Owner Only)
    - `warn <user> <reason>`: Warns a user
    - `warnings <user>`: Shows the number of warnings a user has
    - `clearwarnings <user>`: Clears all warnings for a user
    - `kick <user> <reason>`: Kicks a user
    - `ban <user> <reason>`: Bans a user

    
    """
        pages = [help_text[i:i+1000] for i in range(0, len(help_text), 1000)]
        for i, page in enumerate(pages):
            embed = discord.Embed(title="Help", color=0x00ff00)
            embed.add_field(name="General Commands" if i == 0 else " ", value=page, inline=False)
            if i == 0:
                embed.add_field(name="Admin Commands", value="", inline=False)
            await ctx.respond(embed=embed)

            
def setup(bot):
    bot.add_cog(help(bot))
