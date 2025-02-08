import discord
from discord.ext import commands
from discord import app_commands
import json
import os

class Money(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.money_data = self.load_money_data()

    def load_money_data(self):
        try:
            if os.path.exists('data/money.json'):
                with open('data/money.json', 'r') as f:
                    data = f.read()
                    if not data:
                        return {}
                    return json.loads(data)
            else:
                return {}
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error loading money data: {e}")
            return {}

    def save_money_data(self):
        with open('data/money.json', 'w') as f:
            json.dump(self.money_data, f, indent=4)

    @commands.command(name="balance", help="Check your balance.")
    async def balance(self, ctx):
        user_id = str(ctx.author.id)
        user_data = self.money_data.get(user_id, {"username": ctx.author.name, "amount": 0})
        await ctx.send(f"{ctx.author.mention}, your balance is {user_data['amount']} coins.")

    @commands.command(name="earn", help="Earn some coins.")
    async def earn(self, ctx):
        user_id = str(ctx.author.id)
        user_data = self.money_data.get(user_id, {"username": ctx.author.name, "amount": 0})
        user_data["amount"] += 10
        self.money_data[user_id] = user_data
        self.save_money_data()
        await ctx.send(f"{ctx.author.mention}, you earned 10 coins!")

    @commands.command(name="pay", help="Pay another user.")
    async def pay(self, ctx, member: discord.Member, amount: int):
        if amount <= 0:
            await ctx.send("Amount must be positive.")
            return

        user_id = str(ctx.author.id)
        member_id = str(member.id)

        user_data = self.money_data.get(user_id, {"username": ctx.author.name, "amount": 0})
        member_data = self.money_data.get(member_id, {"username": member.name, "amount": 0})

        if user_data["amount"] < amount:
            await ctx.send("You don't have enough coins.")
            return

        user_data["amount"] -= amount
        member_data["amount"] += amount

        self.money_data[user_id] = user_data
        self.money_data[member_id] = member_data
        self.save_money_data()
        await ctx.send(f"{ctx.author.mention} paid {member.mention} {amount} coins.")

    @commands.command(name="leaderboard", help="Show the top 10 users with the most coins.")
    async def leaderboard(self, ctx):
        sorted_users = sorted(self.money_data.items(), key=lambda x: x[1]["amount"], reverse=True)
        leaderboard = "Leaderboard:\n"
        for i, (user_id, user_data) in enumerate(sorted_users[:10]):
            user = ctx.guild.get_member(int(user_id))
            if user:
                leaderboard += f"{i + 1}. {user_data['username']}: {user_data['amount']} coins\n"
        await ctx.send(leaderboard)

    @app_commands.command(name="balance", description="Check your balance.")
    async def balance_slash(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        user_data = self.money_data.get(user_id, {"username": interaction.user.name, "amount": 0})
        await interaction.response.send_message(f"Your balance is {user_data['amount']} coins.")

    @app_commands.command(name="earn", description="Earn some coins.")
    async def earn_slash(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        user_data = self.money_data.get(user_id, {"username": interaction.user.name, "amount": 0})
        user_data["amount"] += 10
        self.money_data[user_id] = user_data
        self.save_money_data()
        await interaction.response.send_message("You earned 10 coins!")

    @app_commands.command(name="pay", description="Pay another user.")
    async def pay_slash(self, interaction: discord.Interaction, member: discord.Member, amount: int):
        if amount <= 0:
            await interaction.response.send_message("Amount must be positive.")
            return

        user_id = str(interaction.user.id)
        member_id = str(member.id)

        user_data = self.money_data.get(user_id, {"username": interaction.user.name, "amount": 0})
        member_data = self.money_data.get(member_id, {"username": member.name, "amount": 0})

        if user_data["amount"] < amount:
            await interaction.response.send_message("You don't have enough coins.")
            return

        user_data["amount"] -= amount
        member_data["amount"] += amount

        self.money_data[user_id] = user_data
        self.money_data[member_id] = member_data
        self.save_money_data()
        await interaction.response.send_message(f"You paid {member.mention} {amount} coins.")

    @app_commands.command(name="leaderboard", description="Show the top 10 users with the most coins.")
    async def leaderboard_slash(self, interaction: discord.Interaction):
        sorted_users = sorted(self.money_data.items(), key=lambda x: x[1]["amount"], reverse=True)
        leaderboard = "Leaderboard:\n"
        for i, (user_id, user_data) in enumerate(sorted_users[:10]):
            user = interaction.guild.get_member(int(user_id))
            if user:
                leaderboard += f"{i + 1}. {user_data['username']}: {user_data['amount']} coins\n"
        await interaction.response.send_message(leaderboard)

async def setup(bot):
    await bot.add_cog(Money(bot))