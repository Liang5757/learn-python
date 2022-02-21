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

soup = BeautifulSoup(html_sample, 'html.parser')
print(soup.text)

# newsurl = 'https://www.sina.com.cn/'
