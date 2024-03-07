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

class serverinfo(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @slash_command()
    async def serverinfo(
        self,
        ctx: discord.ApplicationContext
    ):
        embed = discord.Embed(title=f"{ctx.guild.name} Info", description="Information of this Server", color=discord.Colour.blue())
        embed.add_field(name='🆔Server ID', value=f"{ctx.guild.id}", inline=True)
        embed.add_field(name='📆Created On', value=ctx.guild.created_at.strftime("%b %d %Y"), inline=True)
        embed.add_field(name='👑Owner', value=f"{ctx.guild.owner.mention}", inline=True)
        embed.add_field(name='👥Members', value=f'{ctx.guild.member_count} Members', inline=True)
        embed.add_field(name='💬Channels', value=f'{len(ctx.guild.text_channels)} Text | {len(ctx.guild.voice_channels)} Voice', inline=True) 
        embed.set_footer(text="Created By SargentRaju")    
        embed.set_author(name=f'{ctx.author.name}')

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(serverinfo(bot))
