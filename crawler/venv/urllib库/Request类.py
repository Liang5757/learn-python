import urllib.request

request = urllib.request.Request('http://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

# class utllib.request.Request(url, data=None,
#                               headers={}, origin_req_host=None,
#                               unverifiable=False, method=None)
# data参数如果要传必须传bytes(字节流)类型的，如果是字典，可以用urllib.parse模块里的urlencode()
# headers是一个字典，它就是请求头，可以通过headers参数直接构造请求，也可以调用请求实例add_header()添加
# origin_req_host指的是请求方的host名称或者IP地址
# unverifiable表示这个请求是否是无法验证的,默认为False，如果我们没有自动抓取图像的权限，值为True
# method是一个字符串，用来指示请求使用的方法

from urllib import request, parse

url = 'http://httpbin.org/post'
# 添加请求头修改User-Agent来伪装成火狐浏览器
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))

# 通过调用add_header()方法添加请求头
# req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')

