import discord
from discord.ext import commands
import os
import random
from dotenv import load_dotenv

class Voz(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='', help='')
    async def nome(self, ctx):

        await ctx.send(response)



def setup(client):
    client.add_cog(Voz(client))
