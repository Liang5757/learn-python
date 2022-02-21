import requests
import re

# r = requests.get('https://www.baodu.com/')
# print(type(r))
# print(r.status_code)
# print(type(r.text))       # str类型
# print(r.cookies)

# data = {
#     'name': 'germey',
#     'age': 22
# }
# r = requests.get('http://httpbin.org/get', params=data)
# print(r.text)
# print(r.json())     # json()方法使JSON格式的字符串转化为字典

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get("https://www.zhihu.com/explore", headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)

# 还可以设置timeout参数:timeout=(5,30)
# 请求分为两个阶段：连接和读取
# timeout会计算两个阶段之和