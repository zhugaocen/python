import requests

def get_text():
    response = requests.get('https://book.qidian.com/info/1017009164#Catalog')
    response.encoding = 'utf-8'
    html = response.text
    print(html)

    title = requests.findall()

get_text()
