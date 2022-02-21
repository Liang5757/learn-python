# coding=utf-8
# r使得字符串默认不转义
print('\n' + r'''hello,\n              
world''')

# 在交互式环境中用...接着上一行输入
# >>> print('''line1
# ... line2
# ... line3''')
# line1
# line2
# line3

# >>> 9 / 3         除法运算结果一定是浮点数
# 3.0

print(ord('A'))         # ord()函数获取字符的整数表示
print(ord('中'))
print(chr(66))          # chr()函数把编码转换为对应的字符
print(chr(25991))

'ABC'.encode('ascii')   # encode()方法可以编码为指定的bytes
x = b'ABC'              # 虽然输出相同但 b 前缀使每个字符只占用一个字节
print(x)
# Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes

b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')        # error='ignore' 忽略错误的字节
# decode()方法使bytes变为str

print('Hi, %s, you have $%d.' % ('Michael', 1000000))        # 用%实现格式化 若要输出%则用%%

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
# format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}

# str是不变对象
a = 'abc'
b = a.replace('a', 'A')             # b = Abc, replace()方法创建了一个新字符串并返回
print(b)
print(a)                            #输出abc


