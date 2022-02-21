dimensions = (200, 50)             #元组定义用小括号
print(dimensions)

#元组中的元素不能修改(指向不能改变)
#但可以通过重新定义来修改
dimensions = (400, 100)
print(dimensions)

#也可以拼接多个元组
dimensions = dimensions + (200, 50)
print(dimensions)

t = (1,)        # 区分小括号和元组的定义

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'          # 元组中的列表中的元素可以修改
t[2][1] = 'Y'
print(t)