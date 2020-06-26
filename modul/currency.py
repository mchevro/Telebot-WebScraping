import requests
import bs4
from bs4 import BeautifulSoup

def currency():
    r = requests.get('https://markets.businessinsider.com/currencies/realtime-chart/usd-idr')
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    post = soup.find_all('div','displayblock text-center text-nowrap')[0].find('span').get_text().replace(',','.')
    hasil = f'<b>USD > IDR</b> : {post}'
    return hasil
