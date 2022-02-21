# filter()把传入的函数依次作用于每个元素，根据返回值是True还是False决定是否保留元素
def is_odd(n):
    return n % 2 == 1

# filter()返回的是Iterator,也就是惰性序列,用list()函数强制获得所有结果
s = list(filter(is_odd, [1, 2, 3, 4, 10, 15]))
print(s)

# filter()完埃式筛法
def _odd_iter():
    n = 1
    while True:
        n += 1
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break

def is_palindrome(num):
    return str(num)[:] == str(num)[::-1]        # [::-1]反转