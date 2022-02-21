# 序列化：把变量从内存中变成可存储或传输

import pickle

f = open('dump.txt', 'wb')

d = dict(name='Bob', age=20, score=88)
pickle.dump(d, f)       # 把对象序列化后(JSON)写入file-like-Object
f = open('dump.txt', 'rb')
infor = pickle.load(f)      # 从file-like-Object中反序列化出对象
print(infor)

f.close()

# dumps()返回标准的JSON
