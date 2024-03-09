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

with open('data/bans.json', encoding='utf-8') as f:
  try:
    bans = json.load(f)
  except ValueError:
    bans = {}
    bans['users'] = []


class ban(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @slash_command(name="ban")
    @commands.has_permissions(administrator=True)
    async def ban(
       self,
       ctx, 
       user:discord.Member, 
       reason: str):
        
        
        bans['users'].append({
            'username': user.name,
            'user_id': user.id,
            'reason': reason
        })
        with open('data/bans.json', 'w', encoding='utf-8') as f:
            json.dump(bans, f, ensure_ascii=False, indent=4)
        await user.send(f"You have been banned for {reason}.")
        await user.ban(reason=reason)
        await ctx.respond(f"{user.mention} has been banned for {reason}.")

    @ban.error
    async def ban_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You cant do that!")

            
def setup(bot):
    bot.add_cog(ban(bot))