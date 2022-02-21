import requests

requests.get("http://httpbin.org/cookies/set/number/123456789")     # 设置了cookies为123456789
r = requests.get('http://httpbin.org/cookies')      # 请求该网站可以获取当前cookies
print(r.text)       # 并没有成功获取cookies

s = requests.Session()      # 设置Session对象
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)      # 成功获取cookies