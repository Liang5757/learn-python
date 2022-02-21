# 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
# f = open('略略略', 'r')

# 文件读写如果产生IOError,f.close()不会调用，可以用try... finally
try:
    f = open('C:/Users/郑靓/Desktop/c学习/码农/printf显示%.cpp', 'r')       # 'rb'可以读取二进制文件，可以增加encoding参数
    print(f.read())     # read()一次性读取全部元素
finally:
    if f:
        f.close()

# 可以用with语句代替
with open('C:/Users/郑靓/Desktop/c学习/码农/printf显示%.cpp', 'r', errors='ignore') as f:# errors表示如果遇到编码错误后如何处理
    print(f.read())

# 用readlines()一次读取一行
# for line in f.readlines():
#     print(line.strip())

# 写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来
# 只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘、
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')
# 'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）
# 传入'a'以追加（append）模式写入