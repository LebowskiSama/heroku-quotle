from brain.drive import driver
from bs4 import BeautifulSoup
from selenium.webdriver.common import keys
import re
import time
from sys import argv

def fetch_name(title):
        
    driver.get('https://google.com/')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.find_element_by_xpath('//*[@title="Search"]').send_keys(title + ' IMDB' + u'\ue007')
    
    #Extract movie/TV_series name
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    movie_name = soup.find('h3', class_='LC20lb').get_text()
    movie_name = movie_name[0:-7]
    
    return movie_name

def fetch_quotes(title):
    
    quotes = []
    
    driver.get('https://google.com/')
    driver.find_element_by_xpath('//*[@title="Search"]').send_keys(title + ' IMDB' + u'\ue007')

    #Navigate to quotes page
    driver.find_element_by_class_name('LC20lb').click()
    time.sleep(1)
    driver.get(driver.current_url + 'quotes')

    #Extract quotes
    soup = BeautifulSoup(driver.page_source, 'html.parser')
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

    return quotes