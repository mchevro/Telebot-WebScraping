import requests
import bs4
from bs4 import BeautifulSoup

def jagatplay():
    r = requests.get('https://jagatplay.com/')
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    post = soup.find_all('h1','news-title t-shadow')[0].find('strong').text
    link = soup.find_all('h1','news-title t-shadow')[0].find('a')['href']
    hasil = f'<b>✏️ Topic</b> : {post}\n\n<b>➡️ Full Artikel</b> : {link}'
    return hasil