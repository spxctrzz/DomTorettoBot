import discord
from discord.ext import commands
import random
import json

client = commands.Bot(command_prefix = 'd!')

with open('config.json', 'r') as json_file:
    config = json.load(json_file)

@client.event
async def on_ready():
    print('-- successfully started bot --')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if 'family' in message.content.lower():
        await message.channel.send(random.choice(config.get("phrases")))

client.run('ENTER BOT TOKEN HERE')