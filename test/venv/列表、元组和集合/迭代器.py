from collections.abc import Iterable, Iterator

# 可作用于for循环的对象都是可迭代对象(Iterable)
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器(Iterator)
# list、dict、str都是可迭代对象(Iterable),但不是迭代器(Iterator)
# 可以调用iter()方法使可迭代对象(Iterable)变为迭代器(Iterator)
print(isinstance(iter([]), Iterator))     # isinstance()方法判断一个对象是否是Iterator

# 迭代器对象表示一个数据流(也可以看成有序序列)，却不能提前知道序列的长度
# 只能不断通过next()方法实现按需计算下一个数据
# 所以迭代器的计算是惰性的，只有在需要返回下一个数据时他才会计算

# for循环本质上是通过不断调用next()实现的