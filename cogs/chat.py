import discord
from discord.ext import commands

# Opcionais:
import os
import random
from dotenv import load_dotenv

class Chat(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Comandos
    @commands.command(name='bootstrap')
    async def bootstrap(self, ctx):
        embed = discord.Embed(
            title="Tile", 
            description="Desc", 
            color= discord.Colour.blue()
        )

        embed.set_footer(text='footer')
        embed.set_image(url="./images/20171117-000.jpg")
        embed.set_thumbnail(url="./images/20171117-000.jpg")
        embed.set_author(name="Autor", icon_url="./images/20171117-000.jpg")

        embed.add_field(name='Campo 1', value='Valor 1', inline=True)
        embed.add_field(name='Campo 2', value='Valor 2', inline=False)
        embed.add_field(name='Campo 3', value='Valor 3', inline=True)

        await ctx.send(embed=embed)
    
    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send('Pong!')
def setup(client):
    client.add_cog(Chat(client))