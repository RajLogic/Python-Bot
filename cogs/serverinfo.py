import discord
from discord.ext import commands
from discord import app_commands

class ServerInfo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="serverinfo", description="Displays information about the server")
    async def serverinfo(self, ctx: commands.Context):
        guild = ctx.guild
        embed = discord.Embed(
            title=f"{guild.name} Info",
            description="Information about this server",
            color=discord.Colour.blue()
        )
        embed.add_field(name='🆔 Server ID', value=f"{guild.id}", inline=True)
        embed.add_field(name='📆 Created On', value=guild.created_at.strftime("%b %d %Y"), inline=True)
        embed.add_field(name='👑 Owner', value=f"{guild.owner.mention}", inline=True)
        embed.add_field(name='👥 Members', value=f'{guild.member_count} Members', inline=True)
        embed.add_field(name='💬 Channels', value=f'{len(guild.text_channels)} Text | {len(guild.voice_channels)} Voice', inline=True)
        embed.set_footer(text="Created By SargentRaju")
        embed.set_author(name=f'{ctx.author.name}')

        await ctx.send(embed=embed)

    @serverinfo.error
    async def serverinfo_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("An error occurred while trying to get server information.")
        else:
            await ctx.send("An unexpected error occurred.")
            raise error  # Re-raise the error for logging
        
    @app_commands.command(name="serverinfo", description="Displays information about the server")
    async def serverinfo_slash(self, interaction: discord.Interaction):
        guild = interaction.guild
        embed = discord.Embed(
            title=f"{guild.name} Info",
            description="Information about this server",
            color=discord.Colour.blue()
        )
        embed.add_field(name='🆔 Server ID', value=f"{guild.id}", inline=True)
        embed.add_field(name='📆 Created On', value=guild.created_at.strftime("%b %d %Y"), inline=True)
        embed.add_field(name='👑 Owner', value=f"{guild.owner.mention}", inline=True)
        embed.add_field(name='👥 Members', value=f'{guild.member_count} Members', inline=True)
        embed.add_field(name='💬 Channels', value=f'{len(guild.text_channels)} Text | {len(guild.voice_channels)} Voice', inline=True)
        embed.set_footer(text="Created By SargentRaju")
        embed.set_author(name=f'{interaction.user.name}')

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(ServerInfo(bot))
