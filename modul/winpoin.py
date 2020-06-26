import requests
import bs4
from bs4 import BeautifulSoup

def winpoin():
    url     = requests.get('https://winpoin.com/')
    soup    = bs4.BeautifulSoup(url.text,'html.parser')
    post    = soup.find_all('div','item-details')[0].find('a').get_text()
    link    = soup.find_all('div','item-details')[0].find('a')['href']
    hasil   = f'<b>✏️ Topic</b> : {post}\n\n<b>➡️ Full Artikel</b> : {link}'
    return hasil