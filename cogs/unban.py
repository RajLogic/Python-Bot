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

with open('Bot-Python/data/bans.json', encoding='utf-8') as f:
  try:
    bans = json.load(f)
  except ValueError:
    bans = {}
    bans['users'] = []
class unban(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @slash_command(name='unban')
    @commands.has_permissions(administrator=True)
    async def unban(
        self,
        ctx: discord.ApplicationContext,
        user: discord.User, reason: str
    ):
        bans['users'] = [entry for entry in bans['users'] if entry['user_id'] != user.id]
        with open('Bot-Python/data/bans.json', 'w', encoding='utf-8') as f:
            json.dump(bans, f, ensure_ascii=False, indent=4)
        await ctx.guild.unban(user, reason=reason)
        await ctx.respond(f"{user.mention} has been unbanned.")

    @unban.error
    async def unban_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You cant do that!")

def setup(bot):
    bot.add_cog(unban(bot))
