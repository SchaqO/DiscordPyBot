import discord
import os
import sys

sys.path.insert(0, '/features')
from dotenv import load_dotenv

from features.quotes import *

load_dotenv()
AUTH_TOKEN = os.getenv('AUTH_TOKEN')

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print('Logged in as name {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send('this is kinda weird')

    if message.content.startswith("finally, bo awanday pe chw"):
        await message.channel.send('da gu bxo hatiw, har awanday pe ache')

    if message.content.startswith("$quote"):
        quote = getQuote()
        await message.channel.send(quote)

client.run(AUTH_TOKEN)
