import discord
import init
import inspirational as insp
import os
import piropo as prp
from keep_alive import keep_alive
import phrase_generator as pg


TOKEN = os.environ['token']
client = discord.Client()


def check_msg_piropo(message):
  l=[
    '!engata-me',
    '!engata me',
    '!engatame',
    '!conta-me a nova',
    '!conta me a nova',
    '!contame a nova',
    '!piropo'
  ]
  return check_list_for_message(l,message)


def check_inspire(message):
  l=[
    '!inspire',
    '!inspira-me',
    '!inspira me',
    '!inspirame'
  ]
  return check_list_for_message(l,message)


def check_list_for_message(l,message):
  for word in l:
    if message.content.startswith(word):
      return True
  return False
  

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  m_content=message.content
  m_channel=message.channel
  if message.author==client.user:
    return
  if m_content.startswith('!hello'):
    await m_channel.send('Sup Bitch')
  elif m_content.startswith('!segmentation fault'):
    await m_channel.send('Só se for no teu cérebro')
  elif check_inspire(message):
    await m_channel.send('Dá-me uns segundos...')
    await m_channel.send(insp.getinspirationalimage())
  elif check_msg_piropo(message):
    #await m_channel.send(message.author.mention)
    #await message.author.send("oi aí")
    await m_channel.send(prp.get_piropo())
  elif m_content.startswith('!olha esta'):
    piropo=m_content.split('!olha esta ',1)[1]
    prp.add_piropo(piropo)
    await m_channel.send('Aprendido, oh Romeu')
  elif m_content.startswith('!esquece'):
    new_l=[]
    if prp.contains_key():
      index= int(m_content.split('!esquece',1)[1])
      prp.delete_piropo(index)
      new_l=prp.get_all_piropos()
    await  m_channel.send(new_l)
  elif m_content.startswith('!todos os piropos'):
    new_l=[]
    new_l=prp.get_all_piropos()
    await m_channel.send(new_l)
  elif m_content.startswith('!ingal'):
    await m_channel.send('Give a moment... Take it eases, alrite?...')
    phrase="\""+pg.get_phrase()+"\" - Truth Bot"
    await m_channel.send(phrase)
      

def main():
  init.init_piropos()
  keep_alive()
  client.run(TOKEN)


if __name__ == "__main__":
  main()