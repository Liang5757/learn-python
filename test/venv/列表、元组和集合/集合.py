# set是一组key的集合，不存储value
# 要创建一个set，需要提供一个list作为输入集合
s = set([3, 1, 2, 2, 3])        #互异性
print(s)

# add(key)方法可以添加元素到set
s.add(4)
s.add(4)           # 仍满足互异性
print(s)

# remove(key)方法可以删除元素
s.remove(1)
# s.remove(1)   若集合无该元素，则报错
print(s)

s2 = set([1, 5, 6, 2])
s3 = s2 & s         #取交集
print(s3)
print(s2 | s)       #取并集

