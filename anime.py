import discord
import os
import requests as rq
import json
import random
from replit import db

client = discord.Client()

c1_words = ["slice of life", "wholesome"]
c2_words = [""]

starter_ani = ["https://www.imdb.com/title/tt1913273/","https://myanimelist.net/anime/6574/Hanamaru_Youchien", "https://myanimelist.net/anime/16417/Tamako_Market"]

def update_ani(ani_msg):
  if "ani" in db.keys():
    ani = db['ani']
    ani.append(ani_msg)
    db['ani'] = ani
  else:
    db['enco'] = [ani_msg]

def del_ani(index):
  ani = db['ani']
  if len(ani) > index:
    del ani[index]
    db['ani'] = ani

@client.event 
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event 
async def on_message(msg):
  if msg.author == client.user:
    return
  
  m = msg.content

  options = starter_ani
  if 'ani' in db.keys():
    options = options + starter_ani
  
  if any(word in m for word in c1_words):
    await msg.channel.send(random.choice(options))
  
  if any(word in m for word in c2_words):
    await msg.channel.send(random.choice(options))
  
  if m.startswith("$new"):
    enco_msg = m.split("$new ",1)[1]
    update_ani(enco_msg)
    await msg.channel.send("new Encouraging message added.")
  
  if m.startswith("$del"):
    ani = []
    if 'ani' in db.keys():
      index = int(m.split("$del",1)[1])
      del_ani(index)
      ani = db['ani']
    await msg.channel.send(ani)
  
  if m.startswith("$list"):
    ani = []
    if 'ani' in db.keys():
      ani = db['ani']
    await msg.channel.send(ani)
  
  if m.startswith("$res"):
    value = m.split("$res ",1)[1]

    if value.lower() == "true":
      db["res"] = True
      await msg.channel.send("Bot is responding!")
    else:
      db["res"] = False
      await msg.channel.send("Bot is currently not responding!!")
    


client.run(os.getenv("Token"))
    