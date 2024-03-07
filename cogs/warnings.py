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

with open('Bot-Python/data/reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []

class warnings(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @slash_command(name="warnings")
    @commands.has_permissions(administrator=True)
    async def warnings(
        self,
        ctx,
        user: discord.User
    ):
        user_warnings = [entry for entry in report['users'] if entry['user_id'] == user.id]
        num_warnings = len(user_warnings)
        await ctx.respond(f"{user.mention} has {num_warnings} warnings.")

    @warnings.error
    async def warnings_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You cant do that!")
def setup(bot):
    bot.add_cog(warnings(bot))