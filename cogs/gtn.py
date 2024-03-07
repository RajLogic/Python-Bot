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

class gtn(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @slash_command(name='guessthenumber')
    async def gtn(
        self, 
        ctx,
        num,
    ): 
        #A Slash Command to play a Guess-the-Number game.

        await ctx.respond('Guess a number between 1 and 10.')
        guess = int(num)

        if int(guess.content) == 5:
            await ctx.send('You guessed it!')
        else:
            await ctx.send('Nope, try again.')
def setup(bot):
    bot.add_cog(gtn(bot))
