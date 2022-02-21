import prettytable as pt


# 时间字符串转[hour, min]
def String2Time(Stime):
    return [int(x) for x in Stime.split(':')]


# [hour, min]转字符串
def time2String(time, ntime=0):
    time = [int(x) for x in time]
    time[1] += (ntime)
    min_carry = int(time[1] / 60)
    if min_carry >= 1:
        time[0] += min_carry
        time[1] -= min_carry * 60

    hour_carry = int(time[0] / 60)
    if hour_carry > 1:
        time[0] -= hour_carry * 24

    return ':'.join(str(x) for x in time)


# 首次适应算法
class Block(object):
    def __init__(self, start, end, length, state, Job):
        self.start = start
        self.end = end
        self.length = length
        self.state = state  # state为1为分配
        self.Job = Job  # 作业


# 分区
def FF_alloc(Job, size):
    for i in range(len(blockList)):
        block = blockList[i]
        if block.state == 0 and block.length > size:
            newBlock = Block(block.start, block.start + size - 1, size, 1, Job)
            freeBlock = Block(block.start + size, block.end, block.length - size, 0, 0)
            del blockList[i]
            blockList.insert(i, freeBlock)
            blockList.insert(i, newBlock)
            return True
        elif block.state == 0 and block.length == size:
            block.state = 1
            return True
    return False


def free(Job):
    for i in range(len(blockList)):
        if blockList[i].Job.name == Job.name:
            blockList[i].state = 0

            # 向前合并空闲块
            if i - 1 > 0 and blockList[i - 1].state == 0:
                freeBlock = Block(
                    blockList[i - 1].start, blockList[i].end,
                    blockList[i - 1].length + blockList[i].length, 0, 0)
                del blockList[i - 1]
                del blockList[i - 1]
                blockList.insert(i - 1, freeBlock)
                i = i - 1

            # 向后合并空闲块
            if i + 1 < len(blockList) and blockList[i + 1].state == 0:
                freeBlock = Block(
                    blockList[i].start, blockList[i + 1].end,
                    blockList[i].length + blockList[i + 1].length, 0, 0)
                del blockList[i]
                del blockList[i]
                blockList.insert(i, freeBlock)

            break


class Job(object):
    def __init__(self, name, atime, ntime, men, mac, state=0):
        self.name = name  # 作业名
        self.atime = atime  # 达到时间
        self.ntime = ntime  # 需要的运行时间
        self.men = men  # 所需内存
        self.mac = mac  # 磁带机需要
        self.state = state  # 状态位 0:未装入内存 1:装入内存未执行 2:完成

        self.ztime = 0  # 周转时间
        self.ftime = ''  # 完成时间
        self.order = 0  # 完成次序

    # 获得到达时间 [hour, min]
    def getATime(self):
        return String2Time(self.atime)

    # 获得完成时间
    def getFTime(self):
        return String2Time(self.ftime)

    # 设置完成时间
    def setFTime(self, ctime):
        self.ftime = time2String(String2Time(ctime), self.ntime)

    # 设置周转时间
    def setZTime(self):
        FTime = self.getFTime()
        ATime = self.getATime()

        temp = [FTime[0] - ATime[0], FTime[1] - ATime[1]]
        self.ztime = temp[0] * 60 + temp[1]


# 初始化作业列表
def initJobList():
    initInput = [
        ['JOB1', '10:00', 25, 15, 2],
        ['JOB2', '10:20', 30, 60, 1],
        ['JOB3', '10:30', 10, 50, 3],
        ['JOB4', '10:35', 20, 10, 2],
        ['JOB5', '10:40', 15, 30, 2]
    ]
    for item in initInput:
        temp = Job(name=item[0], atime=item[1], ntime=item[2], men=item[3], mac=item[4])
        job_list.append(temp)


# 短作业优先的作业调度
def SJF_job_alloc():
    global mac_num

    for item in job_list:
        minIndex = -1
        minSize = 2147483647
        for (index, item) in enumerate(job_list):
            curTime = String2Time(ctime)
            arriveTime = item.getATime()

            if ((curTime[0] > arriveTime[0]) or (
                    (curTime[0] == arriveTime[0]) and (curTime[1] >= arriveTime[1]))) and item.state == 0:
                if item.men < minSize:
                    minIndex = index
                    minSize = item.men

        # 将获得最小到达时间的Job装入内存并分配磁带机,并加入就绪队列
        if mac_num >= job_list[minIndex].mac and FF_alloc(job_list[minIndex], minSize):
            job_list[minIndex].state = 1
            ready_list.append(job_list[minIndex])
            mac_num = mac_num - job_list[minIndex].mac
        else:
            # 如果磁带机不够或者内存大小不足则跳出作业分配 且 返回false
            return False

    return True


# 先来先服务的作业调度算法
def FCFS_job_alloc():
    global mac_num

    for item in job_list:
        minIndex = -1
        for (index, item) in enumerate(job_list):
            curTime = String2Time(ctime)
            arriveTime = item.getATime()

            if ((curTime[0] > arriveTime[0]) or (
                    (curTime[0] == arriveTime[0]) and (curTime[1] >= arriveTime[1]))) and item.state == 0:
                minIndex = index
                break

        # 将获得最小到达时间的Job装入内存并分配磁带机,并加入就绪队列
        if minIndex != -1 and mac_num >= job_list[minIndex].mac and FF_alloc(job_list[minIndex],
                                                                             job_list[minIndex].men):
            job_list[minIndex].state = 1
            ready_list.append(job_list[minIndex])
            mac_num = mac_num - job_list[minIndex].mac
        else:
            # 如果磁带机不够或者内存大小不足则跳出作业分配 且 返回false
            return False

    return True


# 先来先服务的进程调度
def FF_process_alloc():
    global mac_num, ctime, num, ready_list

    while len(ready_list) != 0:
        item = ready_list.pop(0)
        item.state = 3
        item.setFTime(ctime)
        item.setZTime()
        ctime = time2String(String2Time(ctime), item.ntime)
        # 释放磁带机
        mac_num += item.mac
        # 释放内存
        free(item)
        # 作业完成数加一
        num += 1
        item.order = num


# 短进程优先的进程调度
def SPF_process_alloc():
    global mac_num, ctime, num, ready_list

    for i in ready_list:
        minIndex = -1
        minNtime = 2147483647
        for (index, item) in enumerate(ready_list):
            if item.ntime < minNtime and item.state == 1:
                minIndex = index
                minNtime = item.ntime

        minItem = ready_list[minIndex]
        minItem.state = 3
        minItem.setFTime(ctime)
        minItem.setZTime()
        ctime = time2String(String2Time(ctime), minItem.ntime)
        # 释放磁带机
        mac_num += minItem.mac
        # 释放内存
        free(minItem)
        # 作业完成数加一
        num += 1
        minItem.order = num

    ready_list = []


def print_head():
    print("""
        *******************************\n
        * 姓名：郑靓                    *\n
        * 班级：软件工程一班              *\n
        * 学号：3118004988             *\n
        *******************************\n""")


if __name__ == '__main__':
    # 输出个人信息
    print_head()
    # 磁带机数量
    mac_num = 4
    # 内存区大小
    men_size = 100
    # 初始化内存区
    blockList = []
    init = Block(0, men_size - 1, men_size, 0, 0)
    blockList.append(init)
    # 作业列表
    job_list = []
    # 就绪队列
    ready_list = []

    # 初始化作业列表
    initJobList()
    # 初始化当前时间
    ctime = '10:00'

    choice = input('选择作业调度方式 1:先来先服务 2:最小作业优先算法:\n')
    if choice == '1':
        job_alloc = FCFS_job_alloc
    else:
        job_alloc = SJF_job_alloc

    choice = input('选择进程调度方式 1:先来先服务 2:短进程优先:\n')
    if choice == '1':
        process_alloc = FF_process_alloc
    else:
        process_alloc = SPF_process_alloc

    num = 0
    while num < len(job_list):
        # 作业及内存分配
        job_alloc()
        # 进程分配
        process_alloc()

    # 周转时间总和
    sum_ztime = 0

    # 输出信息
    tb = pt.PrettyTable()
    tb.field_names = ['完成次序', "进程名", "到达时间", "所需时间", "主存", "磁带机", "完成时间", "周转时间"]
    for item in job_list:
        sum_ztime += item.ztime
        tb.add_row([item.order, item.name, item.atime, item.ntime, item.men, item.mac, item.ftime, item.ztime])
    print(tb)

    print("平均周转时间：", sum_ztime / len(job_list))
