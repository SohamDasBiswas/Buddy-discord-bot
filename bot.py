import discord,requests, sys, webbrowser, bs4
import os
import pyjokes
import requests
import json
from dotenv import load_dotenv
from lxml import etree
from discord.ext import *
from discord.ext import commands
from discord.ext.commands import Bot
from keep_alive import keep_alive
import random

client = discord.Client()
def get_quote():                            #========================================Quote
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return(quote)

def get_dadjoke():                          #========================================Dadjoke
  response=requests.get("https://us-central1-dadsofunny.cloudfunctions.net/DadJokes/random/jokes")
  json_data = json.loads(response.text)
  joke= json_data['setup'] + "\n" + json_data['punchline']
  return(joke)

def get_affirmations():                     #========================================Affermation
  response=requests.get("https://www.affirmations.dev/")
  data=json.loads(response.text)
  affirmation=data['affirmation']
  return(affirmation)

def jokes():                              #========================================Buddyjokes
  joke= pyjokes.get_joke()
  return joke


def get_trivia(number):                   #========================================Trivia
  url = "https://numbersapi.p.rapidapi.com/"+str(number)+"/trivia"
  querystring = {"fragment":"true","notfound":"floor","json":"true"}
  headers = {
    'x-rapidapi-key': os.getenv('RAPID_KEY'),
    'x-rapidapi-host': "numbersapi.p.rapidapi.com"
  }
  response = requests.request("GET", url, headers=headers, params=querystring)
  json_data = json.loads(response.text)
  trivia= json_data['text']
  return(trivia)

def get_chucknorris():                    #========================================Chucknorris
  url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"
  load_dotenv() 
  headers = {
    'accept': "application/json",
    'x-rapidapi-key': os.getenv('RAPID_KEY2'),
    'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
    }
  response = requests.request("GET", url, headers=headers)
  json_data=json.loads(response.text)
  return json_data

def get_roast():                          #========================================Roast
  response=requests.get("https://insult.mattbas.org/api/insult")
  roast=response.text
  return(roast)

def get_geekjoke():                       #========================================GreekJokes
  response = requests.get("https://geek-jokes.sameerkumar.website/api?format=json")
  json_data = json.loads(response.text)
  geekjoke=json_data["joke"]
  return(geekjoke)

def get_pokemon(pokemon):                 #========================================Pokemon
  response=requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
  if(response.text=="Not Found"):
    return "notfound"
  json_data=json.loads(response.text)
  pokemon_image_url=json_data["sprites"]["front_default"]
  return(pokemon_image_url)

def get_news():                           #========================================News
  url = "https://google-news1.p.rapidapi.com/top-headlines"
  load_dotenv()
  querystring = {"country":"INDIA","lang":"en","limit":"50","media":"true"}

  headers = {
      'x-rapidapi-key': os.getenv('NEWS_API'),
      'x-rapidapi-host': "google-news1.p.rapidapi.com"
      }

  response = requests.request("GET", url, headers=headers, params=querystring)
  json_data=json.loads(response.text)
  return json_data


def chatbot(text):
  url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"
  querystring = {"bid":"178","key":os.getenv('BOT_KEY2'),"uid":"mashape","msg":text}
  headers = {
    'x-rapidapi-key': os.getenv('BOT_KEY'),
    'x-rapidapi-host': "acobot-brainshop-ai-v1.p.rapidapi.com"
    }
  response = requests.request("GET", url, headers=headers, params=querystring)
  json_data=json.loads(response.text)
  answer=json_data['cnt']
  return answer
  
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable","motivate"]
funny_words=["lol","lmao","haha","XD","xD","xd","Xd","Lmao","LMAO","Lol"]
funny_answers=["That was so funny!","Haha","\U0001F923","\U0001F606","Lol","LMAO"]
bad_words=["fuck","Fuck","Asshole","asshole"]
bad_answers=["Common ! No swearing!!","Oye ! Thand Rakh!!","Bruh ! We don't do that here!!","Hey ! Don't say these things!!"]
bad_bots=["bad bot","Bad Bot","bad Bot","Bad bot","gu bot","Gu Bot","gu Bot","Gu bot"]
bad_bot_reply=["\U0001F62D \n Why am I here? Just to suffer."]
good_bots=["good bot","Good bot","good Bot","Good Bot"]
good_bot_reply=["\U0001F60D \n Thank You. Love you."]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('|hello'):                        #========================================hello
        await message.channel.send('Hello '+message.author.name+"!!")

    elif message.content.startswith('|introduce' or "Who made you"):  #========================================Introduce
        await message.channel.send('Hi! I am Buddy. Developed by Soham.')

    elif message.content.startswith('|inspire'):                      #========================================Inspire
      quote = get_quote()
      await message.channel.send(quote)

    elif any(word in message.content for word in sad_words):          #========================================Sad_Words
      affirmation=get_affirmations()+".\nCheer up!"
      await message.channel.send(affirmation)

    elif any(word in message.content for word in funny_words):        #========================================Funny_Words
      await message.channel.send(random.choice(funny_answers))

    elif any(word in message.content for word in bad_words):          #========================================BadWords
      list1=random.choice(bad_answers).split(" ")
      str2=list1[0]
      list1.remove(list1[0])
      res=str2+" "+message.author.name+" ".join(list1)
      await message.channel.send(res)

    elif message.content.startswith('|dadjoke'):                      #========================================dadjoke
      try:
        joke = get_dadjoke()
        await message.channel.send(joke)
      except:
        await message.channel.send("Sorry. There has been a server error.")

    elif message.content.startswith('|geekjoke'):                     #========================================Greekjoke
      geekjoke = get_geekjoke()
      await message.channel.send(geekjoke)

    elif message.content.startswith('|Buddy'):                        #========================================Buddy
      list1=message.content.split(" ")
      text=" ".join(list1[1:])
      answer=chatbot(text)
      await message.channel.send(answer)

    elif message.content.startswith('|buddyjoke'):                    #========================================Buddyjoke
      joke=jokes()
      await message.channel.send(joke)

    elif message.content.startswith('|trivia'):                       #========================================Trivia
      try:
        list1=message.content.split(" ")
        trivia=get_trivia(int(list1[1]))
        await message.channel.send(trivia.capitalize()+".")
      except:
        await message.channel.send("There has been an error with your command.\n The correct command is '|trivia [number]'")

    elif message.content.startswith('|sourcecode'):                  #========================================Source_Code
      embed=discord.Embed(
        title='Buddy Bot Source Code',
        colour=discord.Colour.green()
      )
      embed.set_footer(text='Developed by Soham.')
      embed.set_author(name="Buddy",
      icon_url="https://image.freepik.com/free-vector/cute-funny-white-robot-chat-bot-modern-flat-cartoon-character-illustration-isolated-blue-background-voice-support-service-chat-bot-virtual-online-help-customer-support_92289-946.jpg")
      embed.set_image(url="https://image.freepik.com/free-vector/cute-funny-white-robot-chat-bot-modern-flat-cartoon-character-illustration-isolated-blue-background-voice-support-service-chat-bot-virtual-online-help-customer-support_92289-946.jpg")
      embed.add_field(name="Language Used",value="Python",inline=False)
      embed.add_field(name="Link",value="https://github.com/SohamDasBiswas/Buddy_discord_bot",inline=False)
      await message.channel.send(embed=embed)

    elif message.content.startswith('|pokemon'):                    #========================================Pokemon
      list1=message.content.split(" ")
      pokemon=list1[1]
      if pokemon=="Buddy" or pokemon=="buddy" or pokemon=="Buddy#9784" or pokemon=="@Buddy#9784":
        await message.channel.send("Fuck You")
      else:
        pokemon_image_url=get_pokemon(pokemon)
      if(pokemon_image_url=="notfound"):
        await message.channel.send("Pokemon Not Found")
      else:
        await message.channel.send(pokemon_image_url)

    elif message.content.startswith('|news'):                      #========================================News
      data=get_news()
      list1=message.content.split(" ")
      try:
        num=int(list1[1])
      except:
        num=5
      i = 1
     
      for item in data['articles']:
        if not(item['title']):
          continue
        await message.channel.send(str(i)+". "+item['link'])
        if i == num:
            break
        i += 1

    elif message.content.startswith('|chucknorris'):              #========================================Chucknorris
      json_data=get_chucknorris()
      embed=discord.Embed(
        title='Chuck Norris Meme',
        colour=discord.Colour.blue()
      )
      embed.set_thumbnail(url=json_data["icon_url"])
      embed.add_field(name=json_data["value"],value="CNJ",inline=False)
      await message.channel.send(embed=embed)

    elif message.content.startswith('|roast'):                    #========================================Roast
      def filter(roast):
        roast=roast+" "
        list1=roast.split(" ")
        list2=[]
        for word in list1:
          if word == "You" or word == "you":
            list2.append(message.author.name)
          elif word == "are":
            list2.append("is")
          else:
            list2.append(word)
        return " ".join(list2)
      roast=get_roast()
      roast=filter(roast)
      roast=roast+".\n#roasted\n"
      roast=roast+random.choice(funny_answers)
      await message.channel.send(roast)

    elif message.content.startswith('|roastme'):                  #========================================Roastme
      roast=get_roast()
      roast=roast+".\n#roasted @"+message.author.name+"\n"
      roast=roast+random.choice(funny_answers)
      await message.channel.send(roast)

    elif message.content.startswith('|clear'):                    #========================================Clear
      list1=message.content.split(" ")
      try:
        amount=int(list1[1])
      except:
        amount=5        
      await message.channel.purge(limit=amount)

    elif message.content.startswith('|help'):                     #========================================Helpme
      embed= discord.Embed(title="Here is a list of things I can do!\n",discription="Some useful commands")
      embed.add_field(name="|hello", value="Say Hello.\n",inline=True)
      embed.add_field(name="|help", value="Bot Send's you Commands list and its uses",inline=True)
      embed.add_field(name="|sourcecode", value="Bot will send source code",inline=True)
      embed.add_field(name="|introduce", value="Indroduce Myself.",inline=True)
      embed.add_field(name="|roast @", value="Bot will roast",inline=True)
      embed.add_field(name="|inspire", value="A random inspirational Quote.",inline=True)
      embed.add_field(name="|dadjoke", value="A random dad joke.",inline=True)
      embed.add_field(name="|buddyjoke", value="A random Buddy joke.",inline=True)
      embed.add_field(name="If your message contains", value="**words like sad, depressed, unhappy, miserable- A random affirmative sentence.**", inline=True)
      embed.add_field(name="|trivia [number]", value="A random Trivia for a number.",inline=True)
      embed.add_field(name="|sourcecode", value="Buddy Source Code Link.",inline=True)
      embed.add_field(name="|clear [number]", value="Clears Screen.",inline=True)
      embed.add_field(name="|chucknorris", value="Chuck Norris Joke",inline=True)
      embed.add_field(name="|roastme", value="Roast yourself.",inline=True)
      embed.add_field(name="|geekjoke", value="A random geekjoke.",inline=True)
      embed.add_field(name="|pokemon [name]", value="Displays the given pokemon image.",inline=True)
      embed.add_field(name="|news [number]", value="Displays given number of Indian News Articles.",inline=True)
      embed.add_field(name="Last updated", value="**25th July,2021**",inline=True)
      await message.channel.send(content=None, embed= embed)

    elif any(word in message.content for word in bad_bots):
      await message.channel.send(random.choice(bad_bot_reply))

    elif any(word in message.content for word in good_bots):
      await message.channel.send(random.choice(good_bot_reply))

    elif message.content.startswith('|'):
      await message.channel.send("This command doesn't exist.")


keep_alive()
load_dotenv()      
client.run(os.getenv("TOKEN1"))