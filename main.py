'''
pip install imdbpy
pip install discord.py
pip install py-cord
pip install python-dotenv

'''


'''
This is a simple script that uses IMDbPY to get the 
This script is used to fetch movie data from IMDb and send it as a message in Discord

'''
import discord
from imdb import Cinemagoer
import time
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import  MissingPermissions,has_permissions
import json


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
prefix = os.getenv('DISCORD_PREFIX')
link = os.getenv('DISCORD_LINK')
ownerid = os.getenv('DISCORD_OWNERID')



im = Cinemagoer()
command_prefix="!"
bot = discord.Bot(command_prefix="!", intents=discord.Intents.all())

with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []



@bot.event
async def on_ready():
    print("----------------------")
    print("Logged In As")
    print("Username: %s"%bot.user.name)
    print("ID: %s"%bot.user.id)
    print("----------------------")
    print(command_prefix)

#COGS
#This loads the cogs like in line 16

#works
@bot.slash_command(name='ping')
async def ping(ctx):
    print("ping")
    await ctx.respond("I did something")
    #See if The Bot is Working#
    pingtime = time.time()
    pingms = await ctx.send("Pinging...")
    ping = time.time() - pingtime
    await ctx.send(":ping_pong:  time is `%.01f seconds`" % ping)

#works
@bot.slash_command(name='hello')
async def hello(ctx):
    await ctx.respond("Hello!")
#works
@bot.slash_command(name='botinvite')
async def botinvite(ctx):
    #A Link To Invite This Bot To Your Server!#
    await ctx.respond("Check Your Dm")
    await ctx.author.send(link)
#works
@bot.slash_command(pass_context=True,name='serverinvite')
async def serverinvte(ctx):
    
	"""Pm's A Invite Code (To The Server) To The User"""
	invite = await ctx.channel.create_invite(max_uses=0,unique=False,temporary=False)
	await ctx.author.send("Your invite URL is {}".format(invite.url))
	await ctx.respond("Check Your Dm: ")

#works
@bot.slash_command()
async def serverinfo(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name} Info", description="Information of this Server", color=discord.Colour.blue())
    embed.add_field(name='🆔Server ID', value=f"{ctx.guild.id}", inline=True)
    embed.add_field(name='📆Created On', value=ctx.guild.created_at.strftime("%b %d %Y"), inline=True)
    embed.add_field(name='👑Owner', value=f"{ctx.guild.owner.mention}", inline=True)
    embed.add_field(name='👥Members', value=f'{ctx.guild.member_count} Members', inline=True)
    embed.add_field(name='💬Channels', value=f'{len(ctx.guild.text_channels)} Text | {len(ctx.guild.voice_channels)} Voice', inline=True) 
    embed.set_footer(text="Created By SargentRaju")    
    embed.set_author(name=f'{ctx.author.name}')

    await ctx.send(embed=embed)

#works
@bot.slash_command(pass_context=True, name='setactivity')
async def setgame(ctx, *, activity1):
    """Sets my game (Owner)"""
    if ctx.author.id == (354879221044084737):
        message = ctx.message
        #await ctx.delete()
        await ctx.respond(f"Game was set to **{format(activity1)}**!")
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=activity1))


#works but needs edits
@bot.slash_command(name='movie')
async def movie(ctx, *, arg):
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
        embed.set_author(name=bot.user.name,icon_url=bot.user.avatar.url)
        embed.set_footer(text= "Created By SargentRaju") #icon= "https://cdn.discordapp.com/avatars/354879221044084737/e5c6c1d9899ab42d26848de4dce4bb77.webp")


        await ctx.send_followup(embed=embed)
    except IndexError:
        await ctx.send_followup('No movies found with that title')

    
@bot.slash_command(name="purge",pass_context=True)
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
        await ctx.defer()
        await ctx.channel.purge(limit=limit)
        await ctx.send_followup('Cleared by {}'.format(ctx.author.mention))
        await ctx.message.delete()

@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")
        

@bot.slash_command(name="clear", pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    await ctx.defer()
    await ctx.channel.purge(limit=amount+1)
    await ctx.send_followup(f"Cleared {amount} messages.")


@bot.slash_command(description = "help")
async def help(ctx):
    help_text = """
     General Commands: `all in slash`
    - `help`: Shows this help message
    - `ping`: Shows the bot's latency
    - `serverinvite` : Sends an invite link to our Server
    - `movie <movie name>` : Shows information about a movie
    - `gtn`: Plays a Guess-the-Number game
    - `hello`: Says hello
    - `botinvite`: Sends a link to invite the bot to your server
    - `serverinfo`: Shows information about the server

    
    Moderation Commands (Requires Manage Server Permission):
    Admin Commands: `all in slash`
    - `clear <number>`: Clears a number of messages from the channel
    - `purge <number>`: Purges a number of messages from the channel
    - `purge` : clears chat
    - `setactivity <activity>`: Sets the bot's activity (Owner Only)
    
    """
    pages = [help_text[i:i+1000] for i in range(0, len(help_text), 1000)]
    for i, page in enumerate(pages):
        embed = discord.Embed(title="Help", color=0x00ff00)
        embed.add_field(name="General Commands" if i == 0 else " ", value=page, inline=False)
        if i == 0:
            embed.add_field(name="Admin Commands", value="", inline=False)
        await ctx.respond(embed=embed)

@bot.slash_command()
async def gtn(ctx):
    """A Slash Command to play a Guess-the-Number game."""

    await ctx.respond('Guess a number between 1 and 10.')
    guess = await bot.wait_for('message', check=lambda message: message.author == ctx.author)

    if int(guess.content) == 5:
        await ctx.send('You guessed it!')
    else:
        await ctx.send('Nope, try again.')


bot.run(token)