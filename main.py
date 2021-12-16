import discord
import os
import requests as rq
import json
import random

client = discord.Client()

sad_words = ['anxious', 'depressed', 'sad', 'jobless']

starter_enco = [
  "Cheer up mate!",
  "Hang in there fella",
  "Everything will be alright!",
  "You are the best",
  "You can do it!!"
]

def get_quotes():
  res = rq.get('https://zenquotes.io/api/random')
  json_data = json.loads(res.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return quote

@client.event 
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event 
async def on_message(msg):
  if msg.author == client.user:
    return
  
  m = msg.content

  if m.startswith("$inspire"):
    quote = get_quotes()
    await msg.channel.send(quote)
  
  if any(word in m for word in sad_words):
    await msg.channel.send(random.choice(starter_enco))

client.run(os.getenv("Token"))