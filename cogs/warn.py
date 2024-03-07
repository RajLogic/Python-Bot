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



class warn(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @slash_command(name="warn")
    @commands.has_permissions(administrator=True)
    async def warn(
        self,
        ctx,
        user: discord.User,
        reason: str
        ):
        report['users'].append({
        'username': user.name,
        'user_id': user.id,
        'reason': reason
        })
        with open('Bot-Python/data/reports.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=4)
        await ctx.respond(f"{user.mention} has been warned for {reason}.")
        await user.send(f"You have been warned for {reason}.")

    @warn.error
    async def warn_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You cant do that!")


def setup(bot):
    bot.add_cog(warn(bot))
