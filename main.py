import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

def get_quote():
    response = requests.get('https://animechan.vercel.app/api/random')
    json_data = json.loads(response.text)
    quote = json_data['quote'] + '\n' + '- ' + json_data['character']
    return quote

client = discord.Client()

vc_replies = ['Kye pee li kaanch ki shishi mai, koi nahi hai vc mai', 'Arre arre! VC mai aajao simps.', 'Kaha ho sare weebs?', 'VC VC VC VC VC VC VC VC BC BC VC VC BC BC', 'Simps report for duty.', 'Waifu pillow milegi, VC mai ajao.', 'Ajao ajao ajao!']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$quote'):
        quote = get_quote()
        await message.channel.send(quote)

    if 'vc' in message.content.lower():
        vc_response = random.choice(vc_replies)
        await message.channel.send(vc_response)

keep_alive()
client.run(os.environ['TOKEN'])

