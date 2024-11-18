import discord
from discord.ext import commands
from discord import app_commands

class GuessTheNumber(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="gtn", help="Play a Guess-the-Number game! Guess a number between 1 and 10.")
    async def gtn(self, ctx):
        """Guess-the-Number game."""
        number_to_guess = 5  # Set the target number (can be randomized if desired)
        await ctx.send("I'm thinking of a number between 1 and 10. What's your guess?")

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.isdigit()

        try:
            # Wait for user input
            guess_message = await self.bot.wait_for("message", check=check, timeout=30.0)
            guess = int(guess_message.content)

            if guess == number_to_guess:
                await ctx.send("🎉 You guessed it! Great job!")
            else:
                await ctx.send(f"❌ Nope, the correct number was {number_to_guess}. Better luck next time!")
        except discord.TimeoutError:
            await ctx.send("⏳ You took too long to respond. Game over!")

    @gtn.error
    async def gtn_error(self, ctx, error):
        """Handles errors for the gtn command."""
        if isinstance(error, discord.ext.commands.CheckFailure):
            await ctx.send("You can't play the game in a DM.")
        elif isinstance(error, discord.ext.commands.CommandInvokeError):
            await ctx.send("An error occurred while processing your guess.")
        else:
            await ctx.send("An unexpected error occurred.")
            raise error  # Re-raise for debugging
        
    @app_commands.command()
    async def gtn(self, interaction: discord.Interaction):
        """Guess-the-Number game."""
        number_to_guess = 5  # Set the target number (can be randomized if desired)
        await interaction.response.send_message("I'm thinking of a number between 1 and 10. What's your guess?")

        def check(message):
            return message.author == interaction.user and message.channel == interaction.channel and message.content.isdigit()

        try:
            # Wait for user input
            guess_message = await self.bot.wait_for("message", check=check, timeout=30.0)
            guess = int(guess_message.content)

            if guess == number_to_guess:
                await interaction.response.send_message("🎉 You guessed it! Great job!")
            else:
                await interaction.response.send_message(f"❌ Nope, the correct number was {number_to_guess}. Better luck next time!")
        except discord.TimeoutError:
            await interaction.response.send_message("⏳ You took too long to respond. Game over!")

    @gtn.error
    async def gtn_error(self, interaction: discord.Interaction, error):
        """Handles errors for the gtn command."""
        if isinstance(error, discord.ext.commands.CheckFailure):
            await interaction.response.send_message("You can't play the game in a DM.")
        elif isinstance(error, discord.ext.commands.CommandInvokeError):
            await interaction.response.send_message("An error occurred while processing your guess.")
        else:
            await interaction.response.send_message("An unexpected error occurred.")
            raise error  # Re-raise for debugging

async def setup(bot):
    """Asynchronous cog setup."""
    await bot.add_cog(GuessTheNumber(bot))
