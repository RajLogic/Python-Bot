import discord
from discord.ext import commands
from discord import app_commands
import requests
import os

# Load the weather API key from environment variables
weather_api_key = os.getenv('WEATHER_API_KEY')

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_lat_lon(self, city):
        """Get latitude and longitude for a city."""
        try:
            geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={weather_api_key}"
            response = requests.get(geocode_url)
            response.raise_for_status()
            data = response.json()
            if not data:
                return None, None
            return data[0].get('lat'), data[0].get('lon')
        except requests.RequestException as e:
            print(f"Error fetching geocode data: {e}")
            return None, None

    @commands.command(name="weather", help="Gets the weather information for a city.")
    async def weather(self, ctx, *, city: str):
        """Gets the weather information for a city."""
        lat, lon = self.get_lat_lon(city)
        if lat is None or lon is None:
            await ctx.send(f"City {city} not found.")
            return

        try:
            url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={weather_api_key}&units=metric"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if 'current' not in data:
                await ctx.send(f"Could not retrieve weather data for {city}.")
                return

            current = data['current']
            weather_desc = current['weather'][0]['description']
            temp = current['temp']
            feels_like = current['feels_like']
            humidity = current['humidity']
            wind_speed = current['wind_speed']

            embed = discord.Embed(title=f"Weather in {city}", color=discord.Color.blue())
            embed.add_field(name="Description", value=weather_desc, inline=True)
            embed.add_field(name="Temperature", value=f"{temp}°C", inline=True)
            embed.add_field(name="Feels Like", value=f"{feels_like}°C", inline=True)
            embed.add_field(name="Humidity", value=f"{humidity}%", inline=True)
            embed.add_field(name="Wind Speed", value=f"{wind_speed} m/s", inline=True)
            await ctx.send(embed=embed)
        except requests.RequestException as e:
            await ctx.send(f"Error fetching weather data: {e}")

    @app_commands.command(name="weather", description="Gets the weather information for a city.")
    async def weather_slash(self, interaction: discord.Interaction, city: str):
        """Gets the weather information for a city."""
        lat, lon = self.get_lat_lon(city)
        if lat is None or lon is None:
            await interaction.response.send_message(f"City {city} not found.")
            return

        try:
            url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={weather_api_key}&units=metric"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if 'current' not in data:
                await interaction.response.send_message(f"Could not retrieve weather data for {city}.")
                return

            current = data['current']
            weather_desc = current['weather'][0]['description']
            temp = current['temp']
            feels_like = current['feels_like']
            humidity = current['humidity']
            wind_speed = current['wind_speed']

            embed = discord.Embed(title=f"Weather in {city}", color=discord.Color.blue())
            embed.add_field(name="Description", value=weather_desc, inline=True)
            embed.add_field(name="Temperature", value=f"{temp}°C", inline=True)
            embed.add_field(name="Feels Like", value=f"{feels_like}°C", inline=True)
            embed.add_field(name="Humidity", value=f"{humidity}%", inline=True)
            embed.add_field(name="Wind Speed", value=f"{wind_speed} m/s", inline=True)
            await interaction.response.send_message(embed=embed)
        except requests.RequestException as e:
            await interaction.response.send_message(f"Error fetching weather data: {e}")

async def setup(bot):
    await bot.add_cog(Weather(bot))