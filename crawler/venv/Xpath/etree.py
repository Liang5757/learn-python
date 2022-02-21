from lxml import etree
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get('https://www.zhihu.com/explore', headers=headers)
html = etree.HTML(response)     # 自动修正HTMl文本
print(html)
result = etree.tostring(html)       # 输出修正后的HTML文本(bytes)
# print(result.decode('utf-8'))