import requests
import bs4
from bs4 import BeautifulSoup

def steam():
    url     = requests.get('https://store.steampowered.com/search/?filter=topsellers')
    soup    = bs4.BeautifulSoup(url.text, 'html.parser')
    post    = soup.find_all('div','col search_name ellipsis')[0].find('span').text
    sale    = soup.find_all('div','col search_price discounted responsive_secondrow')[0].find('strike').get_text()
    hasil   = f'<b>Game</b>  : {post}\n<b>Price</b> : {sale}'
    return hasil