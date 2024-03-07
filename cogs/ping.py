import discord
from discord.commands import slash_command
from discord.ext import commands
import time

class ping(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @slash_command(name='ping',description='return bot latency')
    async def ping(self,
        ctx: discord.ApplicationContext
    ):
        print("ping")
        await ctx.respond("I did something")
        #See if The Bot is Working#
        pingtime = time.time()
        pingms = await ctx.send("Pinging...")
        ping = time.time() - pingtime
        await ctx.send(":ping_pong:  time is `%.01f seconds`" % ping)

def setup(bot):
    bot.add_cog(ping(bot))
