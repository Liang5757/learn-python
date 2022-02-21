from collections.abc import Iterable

g = (x * x for x in range(10))      # 生成器(generator)
print(next(g), next(g))         # next()会从头弹出元素，当没有更多的元素时，抛出StopIteration错误
# for n in g:
#     print(n)

# 使用isinstance()判断一个对象是否是Iterable对象
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

def fib_1(max):           # 斐波那契数列
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b         # 相当于t = (b, a+b), a = t[0], b = t[1] (t是一个元组)
        n = n + 1
    return 'done'

# 如果一个函数中含有yield就变成generator
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
# o = odd()
# print(next(o))            # step 1\n 1
# print(next(o))            # step 2\n 3
# print(next(o))            # step 3\n 5

def fib_2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# for n in fib_2(6):
#     print(n)

h = fib_2(6)
while True:
    try:
        x = next(h)
        print('h:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] +L[i+1] for i in range(len(L) - 1)] + [1]