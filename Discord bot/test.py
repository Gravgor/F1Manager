from bs4 import BeautifulSoup
import urllib
import re
import random
import requests

url = "https://www.formula1.com/en/latest.html"
articles = []
respone = urllib.request.urlopen(url)
soup = BeautifulSoup(respone,'lxml')

def getItems():
       for a in soup.findAll('a',attrs={'href': re.compile("/en/latest/article.")}):
           articles.append(a['href'])
       x = random.choice(articles)
       full_string = "https://www.formula1.com"+x
       print(full_string)
       

getItems()