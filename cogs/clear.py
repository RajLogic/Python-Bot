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

class clear(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @slash_command(name="clear",pass_context=True)
    async def clear(
        self,
        ctx: discord.ApplicationContext,
        limit: int
    ):
        await ctx.defer()
        await ctx.channel.purge(limit=limit)
        await ctx.send_followup('Cleared by {}'.format(ctx.author.mention))
        await ctx.message.delete()

    @clear.error
    async def clear_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You cant do that!")


def setup(bot):
    bot.add_cog(clear(bot))
