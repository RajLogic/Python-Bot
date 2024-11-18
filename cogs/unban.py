import discord
from discord.ext import commands
from discord import app_commands
import json

class Unban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.bans_file = 'data/bans.json'
        self.bans = self.load_bans()

    def load_bans(self):
        try:
            with open(self.bans_file, encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, ValueError):
            return {'users': []}

    def save_bans(self):
        with open(self.bans_file, 'w', encoding='utf-8') as f:
            json.dump(self.bans, f, ensure_ascii=False, indent=4)

    @app_commands.command(name='unban')
    @commands.has_permissions(administrator=True)
    async def unban(self, interaction: discord.Interaction, user: discord.User, reason: str):
        self.bans['users'] = [entry for entry in self.bans['users'] if entry['user_id'] != user.id]
        self.save_bans()
        await interaction.guild.unban(user, reason=reason)
        await interaction.response.send_message(f"{user.mention} has been unbanned.")

    @unban.error
    async def unban_error(self, interaction: discord.Interaction, error):
        if isinstance(error, commands.MissingPermissions):
            await interaction.response.send_message("You don't have permission to do that!")

    @commands.command(name='unban')
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, user: discord.User, reason: str):
        self.bans['users'] = [entry for entry in self.bans['users'] if entry['user_id'] != user.id]
        self.save_bans()
        await ctx.guild.unban(user, reason=reason)
        await ctx.send(f"{user.mention} has been unbanned.")


async def setup(bot):
    await bot.add_cog(Unban(bot))
