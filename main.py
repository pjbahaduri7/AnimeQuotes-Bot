import discord
import os
import requests as rq
import json
# import random

client = discord.Client()

def get_quotes():
  url = "https://animechan.vercel.app/api/random"
  res = rq.get(url).json()
  char = res['character']
  anime = res['anime']
  quo = res['quote']
  quote = "ANIME: "+ anime + "\nCHARACTER: " + char + "\nQUOTE: " + quo
  return quote

@client.event 
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event 
async def on_message(msg):
  if msg.author == client.user:
    return
  
  m = msg.content

  if m.startswith("$anime"):
    quote = get_quotes()
    await msg.channel.send(quote)

client.run(os.getenv("ani_token"))

