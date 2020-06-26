import requests
import bs4
from bs4 import BeautifulSoup
import urllib3

def egs():
    page = requests.get('https://www.epicgames.com/store/en-US/free-games')
    soup = BeautifulSoup(page.text, 'html.parser')
    if page.status_code==200:
        content = soup.find('span','OfferTitleInfo-subtitle_ad134671')
    articles = ''
    for i in content.findAll('span'):
        articles = articles + '' + i.text
    return articles