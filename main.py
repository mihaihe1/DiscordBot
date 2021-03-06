import discord
import os
import hiddentoken
import requests
import json
import random

def get_affirmation():
    response = requests.get('https://www.affirmations.dev/')
    json_data = json.loads(response.text)
    return json_data['affirmation']

def get_random_image_nasa():
    rand_sol = random.randint(1, 1000)
    ok = 0
    while ok == 0:
        rand_sol = random.randint(1, 1000)
        url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol='\
              +str(rand_sol)+'&camera=fhaz&api_key='+hiddentoken.nasa_api_key
        response = requests.get(url)
        #print(response)
        json_data = json.loads(response.text)
        #print(json_data)
        photos = json_data['photos']
        #print(photos)
        if photos is not []:
            #print(response)
            return photos[0]['img_src']



    #print(photos[0]['img_src'])

#print(get_random_image_nasa())

client = discord.Client()

@client.event
async def on_ready():
    print('We logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$affirmation'):
        await message.channel.send(get_affirmation())

    if message.content.startswith('$img'):
        await message.channel.send(get_random_image_nasa())



client.run(hiddentoken.token)
