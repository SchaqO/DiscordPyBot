import discord
import os
from dotenv import load_dotenv

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

client.run(AUTH_TOKEN)
