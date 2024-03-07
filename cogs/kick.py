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


with open('data/kicks.json', encoding='utf-8') as f:
  try:
    kicks = json.load(f)
  except ValueError:
    kicks = {}
    kicks['users'] = []

class kick(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @slash_command(name= "kick")
    @commands.has_permissions(administrator=True)
    async def kick(
       self,
       ctx: discord.ApplicationContext,
       user: discord.Member, 
       reason: str
        ):
        
        kicks['users'].append({
            'username': user.name,
            'user_id': user.id,
            'reason': reason
        })
        
        with open('data/kicks.json', 'w', encoding='utf-8') as f:
            json.dump(kicks, f, ensure_ascii=False, indent=4)
        await user.send(f"You have been kicked for {reason}.")
        await user.kick(reason=reason)
        await ctx.respond(f"{user.mention} has been kicked for {reason}.")

    @kick.error
    async def kick_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You cant do that!")


def setup(bot):
    bot.add_cog(kick(bot))
