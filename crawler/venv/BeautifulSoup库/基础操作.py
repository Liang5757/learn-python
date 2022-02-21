import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.sina.com.cn/')

# print(res)                #里面的资讯
# print(res.text)           #显示内容

res.encoding = 'utf-8'              #获取res的编码格式
# print(res.text)                   #打印

html_sample = ' \
<html> \
 <body> \
 <h1 id="title">Hello world</h1> \
 <a href="#" class="link">This is link1</a> \
 <a href="# link2" class="link">This is link2</a> \
 </body> \
</html>'

soup = BeautifulSoup(html_sample, 'html.parser')        # 'html.parser'
print(soup.text)

# 使用select找出含有h1标签的元素
header = soup.select('h1')
print(header)
print(header[0])
print(header[0].text)

# 使用select找出所有id为title的元素(id前面需要加#)
alink = soup.select('#title')
for link in alink:
    print(link.text)

# 使用select找出所有class为link的元素(class前面需要加.)
for link in soup.select('.link'):
    print(link.text)

# 使用selec找出所有a tag的href连结
alinks = soup.select('a')
for link in alinks:
    print(link['href'])
# newsurl = 'https://www.sina.com.cn/'

soup_2 = BeautifulSoup(html_sample, 'lxml')
print(soup_2.prettify())
print(soup_2.title.name)