def lazy_sum(*args):
    def sum():
        ans = 0
        for n in args:
            ans += n
        return ans
    return sum

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
# f1()和f2()的调用结果互不干扰,每次调用都会返回一个新的函数
print(f1 == f2)
print(f1() == f2())