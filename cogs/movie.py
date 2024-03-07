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

im = Cinemagoer()

class movie(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @slash_command(name= "movie")
    async def movie(
        self,
        ctx: discord.ApplicationContext,
        *, arg
    ):
        await ctx.defer()
        search = arg
        results = im.search_movie(search)

        try:
            global title,movies, ID
            title = results[0]
            movies = title.getID()
            ID = im.get_movie(movies)
            cast = [d['name'] for d in ID['cast']]
            genres = [d for d in ID['genres']]
            countries =[d for d in ID['countries']]
            director = [d['name'] for d in ID['directors']]
            languages =[d for d in ID['languages']] 
            rating =ID['rating']
            plot = ID['plot outline']
            title = ID['title']
            year = ID['year']

            topActors = 5
        


            print('\nMovie Information:\n')
            print('Title: ',ID['title'])
            print('Year: ',ID['year'])
            print('Rating: ',ID['rating'],'/10')
            print('Genre: '.join([i for i in ID['genres']]))
            print('Country: ',', '.join([i for i in ID['countries']]))
            print('Language: ',', '.join([i for i in ID['languages']]))
            #print('Director(s): ',ID['directors'])
            print('Top 5 Actors')
            for i in range(5): 
                print("    ", cast[i]) 
        

            embed = discord.Embed(
            
            title=f"Movie  Info - {title}",
            description=f"This is the Information For The Movie {title}",
            color=discord.Color.blue())
            
            embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/724567148030197781/86955239ccb703bd3361cfd8c74d0345.webp")
            embed.add_field(name='Title',value=f"{title} ({year})",inline=True)
            embed.add_field(name="Ratings", value=rating)
            embed.add_field(name="Genre", value=genres)
            embed.add_field(name="Country", value=countries)
            embed.add_field(name="Languages", value=languages)
            embed.add_field(name="Directors", value=director)
            embed.add_field(name="Actors", value=f"{cast[1],cast[2],cast[3],cast[4],cast[5]}")
            #for i in range(5):
                # embed.add_field(name="Actors"[i], value=cast[i])
            embed.add_field(name="Plot",value=plot)
            embed.set_author(name=ctx.user.name,icon_url=ctx.user.avatar.url)
            embed.set_footer(text= "Created By SargentRaju") #icon= "https://cdn.discordapp.com/avatars/354879221044084737/e5c6c1d9899ab42d26848de4dce4bb77.webp")


            await ctx.send_followup(embed=embed)
        except IndexError:
            await ctx.send_followup('No movies found with that title')
def setup(bot):
    bot.add_cog(movie(bot))
