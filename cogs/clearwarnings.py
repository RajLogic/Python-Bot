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

class clearwarnings(commands.Cog):

    def __init__(self,bot):
        self.bot = bot


    @slash_command(name="clearwarnings")
    @commands.has_permissions(administrator=True)
    async def clearwarnings(
        self,
        ctx,
        user: discord.User
        ):
            report['users'] = [entry for entry in report['users'] if entry['user_id'] != user.id]
            with open('Bot-Python/data/reports.json', 'w', encoding='utf-8') as f:
                json.dump(report, f, ensure_ascii=False, indent=4)
            await ctx.respond(f"Warnings cleared for {user.mention}.")
            await user.send("Your warnings have been cleared.")


    @clearwarnings.error
    async def clear_warnings_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You cant do that!")


def setup(bot):
    bot.add_cog(clearwarnings(bot))
