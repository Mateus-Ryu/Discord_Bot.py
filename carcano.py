import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import json

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
default_prefix = os.getenv('DEFAULT_PREFIX')

def get_prefix(client, message):
    with open('prefixes.json', 'r') as file:
        prefixes = json.load(file)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix= get_prefix)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as file:
        prefixes = json.load(file)

    prefixes[str(guild.id)] = default_prefix

    with open('prefixes.json', 'w') as file:
        json.dump(prefixes, file, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as file:
        prefixes = json.load(file)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as file:
        json.dump(prefixes, file, indent=4)

@bot.command(name='mudar_prefix')
async def mudar_prefix(cxt, prefix):
    with open('prefixes.json', 'r') as file:
        prefixes = json.load(file)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as file:
        json.dump(prefixes, file, indent=4)


bot.run(token)
