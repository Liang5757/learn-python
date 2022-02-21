import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)      # current_thread()返回当前线程的实例
t = threading.Thread(target=loop, name='LoopThread')        # 创建子线程
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)