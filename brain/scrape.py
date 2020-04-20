from bs4 import BeautifulSoup
import re
import bs4
import requests

def scrape_quotes(imdbID):

    page = requests.get('https://www.imdb.com/title/' + imdbID + '/quotes')

    #Extract quotes
    quotes = []
    soup = BeautifulSoup(page.content, 'html.parser')
    containers = soup.findAll('div', class_='sodatext')
    # cnt_len = len(containers) - 1

    for container in containers:
        quotes.append('<hr>' + '<br>')
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