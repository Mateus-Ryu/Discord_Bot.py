import discord
from discord.ext import commands

# Opcionais:
import os
import random
from dotenv import load_dotenv

class Default(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Eventos
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game('Girl Frontline'))
        print(f'{self.client.user.name} se conectou ao Discord!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.CheckFailure):
            await ctx.send('Você não tem a role certa para poder pedir esse comando, desculpe-me!')

    # Comandos
    @commands.command(name='load')
    async def load(self, ctx, extension):
        try:
            self.client.load_extension(f'cogs.{extension}')
            await ctx.send(f'Comandante, a extenção "{extension}" foi carregada com sucesso!')
        except:
            await ctx.send(f'Me desculpe comandante, mas não encontrei a extenção "{extension}". Talvez ela já esteja carregado ou nem exista...')

    @commands.command(name='unload')
    async def unload(self, ctx, extension):
        try:
            self.client.unload_extension(f'cogs.{extension}')
            await ctx.send(f'Comandante, a extenção "{extension}" foi descarregada com sucesso!')
        except:
            await ctx.send(f'Me desculpe comandante, mas não encontrei a extenção "{extension}". Talvez ela já esteja descarregado ou nem exista...')
            

    @commands.command(name='reload')
    async def reload(self, ctx, extension):
        try:
            try:
                self.client.unload_extension(f'cogs.{extension}')
                self.client.load_extension(f'cogs.{extension}')
                await ctx.send(f'Comandante, a extenção "{extension}" foi recarregada com sucesso!')
            except:
                self.client.load_extension(f'cogs.{extension}')
                await ctx.send(f'Comandante, a extenção "{extension}" não estava carregada, então apenas o carreguei!')
        except:
            await ctx.send(f'Me desculpe comandante, mas não encontrei a extenção "{extension}". Muito provavelmente ela nem exista...')

    @commands.command(name='limpe', help='Remove as N ultimas mensagens')
    async def limpe(self, ctx, quantidade : int = 1 ):
        if quantidade > 0:
            await ctx.channel.purge(limit=quantidade)
            await ctx.send(f'Eu tentei apagar as {quantidade} últimas mensagens, assim como me pediu!')
        else:
            await ctx.send(f'Por favor comandante, não brinque comigo! É impossivel apagar {quantidade} mensagens...')
        
def setup(client):
    client.add_cog(Default(client))