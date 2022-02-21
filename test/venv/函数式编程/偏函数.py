# 偏函数通过设置函数参数的默认值，来降低函数调用的难度
import functools

int2 = functools.partial(int, base=2)       # partial()把函数的某些参数固定住，并返回一个新函数
# 可以接收 函数对象、*args、**kw

print(int2('100010'))
# int2('100010')相当于kw = {'base': 2}, int('100010', **kw)

max2 = functools.partial(max, 10)       # 10会作为*args部分自动添加到左边，相当于max(10, 5, 6, 7)
print(max2(5, 6, 7))
