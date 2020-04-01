from bs4 import BeautifulSoup
import re
import time
from urllib import request
import requests
import json
import bs4

def parse_titles(string):

    string = string.replace(' ','+')
    #Using OMDb API
    response = request.urlopen('http://www.omdbapi.com/?apikey=d0b356ff&s='+string)
    data = json.loads(response.read())
    Search = data['Search']
    # for item in Search:
    #     print(item['Title'] + ' (' + item['Year'] + ')')
    imdbID = (Search[0]['imdbID'])
    mname = Search[0]['Title'] + ' ' + '(' + Search[0]['Year'] + ')'
    return mname, imdbID

def scrape_quotes(imdbID):

    page = requests.get('https://www.imdb.com/title/' + imdbID + '/quotes')

    #Extract quotes
    quotes = []
    soup = BeautifulSoup(page.content, 'html.parser')
    containers = soup.findAll('div', class_='sodatext')
    # cnt_len = len(containers) - 1

    for container in containers:
        quotes.append('<hr>')
        quotelists = container.findAll('p')

        for quotelist in quotelists:
            quotes.append(quotelist.text)

    quotes.pop(0)  #Remove very first hr tag
    i = 0 #Remove unnecessary new lines

    for quote in quotes:
        x = re.sub('\\n', ' ', quote)
        quotes[i] = x
        i = i + 1

    return(quotes)