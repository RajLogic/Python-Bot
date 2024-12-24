import discord
from discord.ext import commands
from discord import app_commands

class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="userinfo", help="Displays information about a user.")
    async def userinfo(self, ctx, user: discord.User):
        """Displays information about a user."""
        embed = discord.Embed(title=f"User Info - {user.name}", color=discord.Color.blue())
        embed.add_field(name="Username", value=user.name, inline=True)
        embed.add_field(name="Discriminator", value=user.discriminator, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Created At", value=user.created_at.strftime("%b %d %Y"), inline=True)
        embed.set_thumbnail(url=user.avatar.url)
        await ctx.send(embed=embed)

    @app_commands.command(name="userinfo", description="Displays information about a user.")
    async def userinfo_slash(self, interaction: discord.Interaction, user: discord.User):
        """Displays information about a user."""
        embed = discord.Embed(title=f"User Info - {user.name}", color=discord.Color.blue())
        embed.add_field(name="Username", value=user.name, inline=True)
        embed.add_field(name="Discriminator", value=user.discriminator, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Created At", value=user.created_at.strftime("%b %d %Y"), inline=True)
        embed.set_thumbnail(url=user.avatar.url)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(UserInfo(bot))