"""
小说内容爬取：顶点小说网http://www.ddxsku.com/
1.设置请求头
2.设置爬取得url
3.设置保存小说的路径
4.获取小说内容并保存
5.编写入口函数
"""

import requests
from lxml import etree

# 获取要爬取的urls

urls = ['http://www.ddxsku.com/files/article/html/51/51443/{}.html'.format(i) for i in range(22257405, 22257415)]

# for url in urls:
#     print(url)

# 设置保存小说的路径
path = r'D:/xiaoshuo/'

# 获取小说内容并保存
def get_text(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    selector = etree.HTML(r.text)
    # 获取文章标题
    title = selector.xpath('//*[@id="amain"]/dl/dd[1]/h1/text()')
    # 获取小说内容
    text = selector.xpath('//*[@id="contents"]/text()')
    # print(path + title[0])
    with open(path + title[0], 'w', encoding='utf-8') as f:
        for i in text:
            f.write(i)

if __name__ == '__main__':
    for url in urls:
        get_text(url)
