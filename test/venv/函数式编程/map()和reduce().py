from functools import reduce

def f(x):
    return x*x

def add(x, y):
    return x+y

r = map(f, [1, 2, 3, 4, 5, 6])      # r是一个惰性序列(Iterator)
print(r)
print(list(r))

# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
h = reduce(add, [1, 2, 3, 4, 5])
print(h)

digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def char2int(s):
#     def fn(x, y):
#         return x*10+y
#     def char2num(s):
#         return digits[s]
#     return reduce(fn, map(char2num, s))

# 上述函数可以用lambda简化为
def char2num(s):
    return digits[s]

def str2int(s):
    return reduce(lambda x, y: x*10+y, map(char2num, s))

print(str2int('413522146'))
