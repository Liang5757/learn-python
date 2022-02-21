import urllib.request
import urllib.parse
import urllib.error
import socket

# response = urllib.request.urlopen('https://www.baidu.com')
# print(response.read().decode('utf-8'))
# print(type(response))       # HTTPResponse类型的对象
# print(response.status) print(response.getheaders())
# print(response.getheader('Server'))

# urllib.parse模块中的urlencode()方法将参数字典转化为字符串
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

# 用timeout参数设置最大响应时间(单位为s)，超出则报错
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
    else:
        print(response.read())




