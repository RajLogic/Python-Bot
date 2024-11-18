import discord
from imdb import Cinemagoer
from discord.ext import commands
from discord import app_commands

im = Cinemagoer()

class Movie(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def create_movie_embed(self, title):
        movie_id = title.getID()
        movie_info = im.get_movie(movie_id)
        cast = [d['name'] for d in movie_info['cast'][:5]]
        genres = movie_info['genres']
        countries = movie_info['countries']
        directors = [d['name'] for d in movie_info['directors']]
        languages = movie_info['languages']
        rating = movie_info['rating']
        plot = movie_info.get('plot outline', 'N/A')
        title = movie_info['title']
        year = movie_info['year']

        embed = discord.Embed(
            title=f"Movie Info - {title}",
            description=f"This is the Information For The Movie {title}",
            color=discord.Color.blue()
        )
        
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/724567148030197781/86955239ccb703bd3361cfd8c74d0345.webp")
        embed.add_field(name='Title', value=f"{title} ({year})", inline=True)
        embed.add_field(name="Ratings", value=f"{rating}/10")
        embed.add_field(name="Genre", value=', '.join(genres))
        embed.add_field(name="Country", value=', '.join(countries))
        embed.add_field(name="Languages", value=', '.join(languages))
        embed.add_field(name="Directors", value=', '.join(directors))
        embed.add_field(name="Top 5 Actors", value=', '.join(cast))
        embed.add_field(name="Plot", value=plot)
        return embed

    @commands.command(name="movie")
    async def movie_command(self, ctx, *, arg: str):
        search = arg
        results = im.search_movie(search)

        if results:
            embed = await self.create_movie_embed(results[0])
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
            embed.set_footer(text="Created By SargentRaju")
            await ctx.send(embed=embed)
        else:
            await ctx.send('No movies found with that title')

    @app_commands.command(name="movie")
    async def movie_slash_command(self, interaction: discord.Interaction, arg: str):
        await interaction.response.defer()
        search = arg
        results = im.search_movie(search)

        if results:
            embed = await self.create_movie_embed(results[0])
            embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url)
            embed.set_footer(text="Created By SargentRaju")
            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send('No movies found with that title')

async def setup(bot):
    await bot.add_cog(Movie(bot))
