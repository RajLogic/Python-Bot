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

link = os.getenv('DISCORD_LINK')

class botinvite(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @slash_command(name='botinvite')
    async def botinvite(
        self,
        ctx: discord.ApplicationContext
    ):
        #A Link To Invite This Bot To Your Server!#
        await ctx.respond("Check Your Dm")
        await ctx.author.send(link)
def setup(bot):
    bot.add_cog(botinvite(bot))