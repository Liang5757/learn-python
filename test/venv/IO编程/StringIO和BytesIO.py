from io import StringIO

f = StringIO()
f.write('hello')        # 返回值为字符个数
f.write(' world!')
print(f.getvalue())     # getvalue()方法用于获得写入后的str

f = StringIO('Hello!\nHi!\nGoodbye!')       # 初始化StringIO
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

from io import BytesIO
from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
