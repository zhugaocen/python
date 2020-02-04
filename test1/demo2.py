#导入三个工具包
import requests
from bs4 import BeautifulSoup
import urllib.request


def get_img():
    #解析网站
    url = requests.get('https://www.buxiuse.com/?page=2')  #爬取网站的url
    #获取网站的数据
    global html
    html = url.text
    #打印输出网站的数据
    # print(html)

#调用函数
get_img()

'''
获取BeautifulSoup对象
HTML 表示被解析的HTML格式的内容
html.praser表示解析用的解析器
'''

soup = BeautifulSoup(html,'html.parser')
girl = soup.find_all('img')
# print(girl)

x = 0
#获取图片路径
for i in girl:
    #获取图片的src路径
    src = i.get('src')
    #下载图片 利用urllib
    urllib.request.urlretrieve(src,'./image/{}.jpg'.format(x))
    x += 1
    print('正在下载第{}张图片'.format(x))