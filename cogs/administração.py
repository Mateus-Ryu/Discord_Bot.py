import discord
from discord.ext import commands

# Opcionais:
import os
import random
from dotenv import load_dotenv

class Administração(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='kick')
    @commands.has_role('admin')
    async def kick(self, ctx, membro : discord.Member, *, motivo=None):
        await membro.kick(reason=motivo)

    @commands.command(name='ban')
    @commands.has_role('admin')
    async def ban(self, ctx, membro : discord.Member, *, motivo=None):
        await membro.ban(reason=motivo)

    @commands.command(name='unban')
    @commands.has_role('admin')
    async def unban(self, ctx, *, membro):
        users_banidos = await ctx.guild.bans()
        nome_membro, id_membro = membro.split('#')

        for entrada in users_banidos:
            user = entrada.user
            if(user.name, user.discriminator) == (nome_membro, id_membro):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} foi desbanido!')
                return

def setup(client):
    client.add_cog(Administração(client))