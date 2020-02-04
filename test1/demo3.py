import requests
from bs4 import BeautifulSoup
import urllib.request
import re

def get_text():
    response = requests.get('https://www.kanshuhai.com/0/5/5218/?btwaf=48623795')
    response.encoding = 'gbk'
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find_all('dd')
    print(title)

get_text()
