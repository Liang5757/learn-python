import requests

r = requests.get("https://github.com/favicon.ico")
with open('favicon.ico', 'wb') as f:
    f.write(r.content)

r = requests.get("http://www.baidu.com")
print(requests.codes.ok)
exit(0) if not r.status_code == requests.codes.ok else print('Request Successfully')
# 比对成功的状态码
