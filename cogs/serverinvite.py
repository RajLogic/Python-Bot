import discord
from discord.ext import commands
from discord import app_commands

class serverinvite(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @app_commands.command(name='serverinvite')
    async def serverinvite(
        self,
        interaction: discord.Interaction
    ):
        invite = await interaction.channel.create_invite(max_uses=0, unique=False, temporary=False)
        await interaction.user.send(f"Your invite URL is {invite.url}")
        await interaction.response.send_message("Check your DM")

    @serverinvite.error
    async def serverinvite_error(self, interaction: discord.Interaction, error):
        if isinstance(error, commands.CommandInvokeError):
            await interaction.response.send_message("An error occurred while trying to send you the server invite link.")
        else:
            await interaction.response.send_message("An unexpected error occurred.")
            raise error  # Re-raise the error for logging
        
    @commands.command(name='serverinvite')
    async def serverinvite(self, ctx):
        invite = await ctx.channel.create_invite(max_uses=0, unique=False, temporary=False)
        await ctx.author.send(f"Your invite URL is {invite.url}")
        await ctx.send("Check your DM")


async def setup(bot):
    await bot.add_cog(serverinvite(bot))
