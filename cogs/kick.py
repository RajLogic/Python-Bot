import json
import discord
from discord.ext import commands
from discord import app_commands


with open('data/kicks.json', encoding='utf-8') as f:
    try:
        kicks = json.load(f)
    except ValueError:
        kicks = {}
        kicks['users'] = []

class Kick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick")
    @commands.has_permissions(administrator=True)
    async def kick(
        self,
        ctx,
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
        await ctx.send(f"{user.mention} has been kicked for {reason}.")


    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You can't do that!")

    

    @app_commands.command(name="kick")
    @commands.has_permissions(administrator=True)
    async def kick(
        self,
        interaction: discord.Interaction,
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
        await interaction.response.send_message(f"{user.mention} has been kicked for {reason}.")

    @kick.error
    async def kick_error(self, interaction: discord.Interaction, error):
        if isinstance(error, commands.MissingPermissions):
            await interaction.response.send_message("You can't do that!")


async def setup(bot):
    await bot.add_cog(Kick(bot))
