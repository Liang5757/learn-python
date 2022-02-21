from multiprocessing import Process, Pool
import os, time, random

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())       # 返回当前进程id， os.getppid()返回父进程id
    p = Process(target=run_proc, args=('test',))        # 传入执行函数， 执行函数的参数
    print('Child process will start')
    p.start()       # 启动进程
    p.join()        # 等待子进程结束后在继续往下进行
    print('Child process end')

# 进程池
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()%2 * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(4):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()       # close()之后就不能再继续添加新的Process
    p.join()        # 必须在join()之前调用close()
    print('All subprocesses done.')
