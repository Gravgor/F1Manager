import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import random
from bs4 import BeautifulSoup
import urllib
from discord import user
from discord.ext.commands.errors import MissingPermissions
import requests
import re

url = "https://www.formula1.com/en/latest.html"
url2 = "https://www.autosport.com/f1/news/"
articles = []
respone = urllib.request.urlopen(url)
soup = BeautifulSoup(respone,'lxml')
respone2 = urllib.request.urlopen(url2)
soup2 =  BeautifulSoup(respone2,'lxml')




client = commands.Bot(command_prefix = '!')
logs_channel = 873019204603891783


@client.event
async def on_ready():
    print("Online {0.user}".format(client))

@client.command(aliases=['news','f1info'])
async def f1news(ctx):
    for a in soup.findAll('a',attrs={'href': re.compile("/en/latest/article.")}):
                 articles.append(a['href'])
    x = random.choice(articles)
    full_string = "https://www.formula1.com"+x    
    await ctx.send('Here you go, yours Formula newest info: ' +full_string)


@client.command()
async def projectinfo(ctx):
            await ctx.reply('To be filled',mention_author=True)




#
# 
# 
# 
# 
# moderators



@has_permissions(kick_members=True)
@client.command()
async def kick(ctx, Member: discord.Member,*,reason=None):
        await Member.kick(reason=reason)
        await ctx.send(f"{Member} was just kicked from the server")


@has_permissions(administrator=True)
@client.command()
async def ban(ctx,Member: discord.Member,*,reason=None):
    await Member.ban(reason=reason)
    await ctx.send(f"{Member} was just banned from the server")




# 
# 
# 
# 
# 
# 
# brak permisji
@client.command()
async def kick_error(error,ctx):
    if isinstance(error,MissingPermissions):
          await ctx.send(MissingPermissions)

@has_permissions(administrator=True)
@client.command()
async def ban_error(error,ctx):
    if isinstance(error,MissingPermissions):
        await ctx.send("You don't have permission to do that")
# 
# 
# 
# 
# 
# 
# 



client.run("ODcyOTUwNzA5NDU1MzEwODc4.YQxUsw.-x3Hm9V_-9X6hyA7lL9at4AGGqk")
