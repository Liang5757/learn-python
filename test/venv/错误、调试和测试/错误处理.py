def foo():
    pass

try:
    print('try...')
    r = 10 / int('2')
    r = 10 / 0
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:           # 如果没有错误，执行该语句块
    print('no error!')
finally:
    print('finally...')
print('END')

# 如果try语句块执行错误，则直接跳转到except语句块，如果有finally，则继续执行finally语句块
# 如果没有执行错误，则跳过except，执行(如果有)finally语句块
# 如果同时有多个错误，执行第一个error的except的语句块

# python的错误也是class，except不止捕获该类型的错误，子类也一网打尽
try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
# 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类


import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)        # 程序打印完错误信息后会继续执行，并正常退出

main()
print('END')

