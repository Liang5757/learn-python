import functools

# 无参装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log            # 等价于 now = log(now), now变量指向新的函数
def now():
    print('2019-3-22')
    print(now.__name__)     # 返回值最终是wrapper()函数

now()

# 含参装饰器
def log_2(text):
    def decorator(func):
        @functools.wraps(func)      # 把原始函数的__name__等属性复制到wrapper()函数中
        def wrapper(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log_2('execute')       # 等价于now_2 = log_2('execute')(now)
def now_2():
    print('2019-3-23')
    print(now_2.__name__)

now_2()

# 多个装饰器装饰一个函数,其执行顺序是从下往上