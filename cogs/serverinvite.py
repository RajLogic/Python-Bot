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

class serverinvite(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @slash_command(pass_context=True,name='serverinvite')
    async def serverinvite(
        self,
        ctx: discord.ApplicationContext
    ):
        invite = await ctx.channel.create_invite(max_uses=0,unique=False,temporary=False)
        await ctx.author.send("Your invite URL is {}".format(invite.url))
        await ctx.respond("Check Your Dm: ")
def setup(bot):
    bot.add_cog(serverinvite(bot))
