import discord
import os
import requests as rq
import json
import random
from replit import db

client = discord.Client()

sad_words = ['anxious', 'depressed', 'sad', 'jobless']

starter_enco = ["Cheer up mate!", "Hang in there fella", "Everything will be alright!", "You are the best", "You can do it!!"]

def get_quotes():
  res = rq.get('https://zenquotes.io/api/random')
  json_data = json.loads(res.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return quote

def update_enco(enco_msg):
  if "enco" in db.keys():
    enco = db['enco']
    enco.append(enco_msg)
    db['enco'] = enco
  else:
    db['enco'] = [enco_msg]

def del_enco(index):
  enco = db['enco']
  if len(enco) > index:
    del enco[index]
    db['enco'] = enco

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

  options = starter_enco
  if 'enco' in db.keys():
    options = options + starter_enco
  
  if any(word in m for word in sad_words):
    await msg.channel.send(random.choice(options))
  
  if m.startswith("$new"):
    enco_msg = m.split("$new ",1)[1]
    update_enco(enco_msg)
    await msg.channel.send("new Encouraging message added.")
  
  if m.startswith("$del"):
    enco = []
    if 'enco' in db.keys():
      index = int(m.split("$del",1)[1])
      del_enco(index)
      enco = db['enco']
    await msg.channel.send(enco)
  
  if m.startswith("$list"):
    enco = []
    if 'enco' in db.keys():
      enco = db['enco']
    await msg.channel.send(enco)
  
  if m.startswith("$res"):
    value = m.split("$res ",1)[1]

    if value.lower() == "true":
      db["res"] = True
      await msg.channel.send("Bot is responding!")
    else:
      db["res"] = False
      await msg.channel.send("Bot is currently not responding!!")
    


client.run(os.getenv("Token"))