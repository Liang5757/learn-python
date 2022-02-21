import prettytable as pt
import sys


# 首次适应算法 and 最佳适应算法
class Block(object):
    def __init__(self, start, end, length, state, id):
        self.start = start
        self.end = end
        self.length = length
        self.state = state  # state为1为分配
        self.id = id  # 任务编号


def input_task():
    choice = int(input("请输入分配方式(1:FF, 2:BF)："))
    if choice == 1:
        alloc = FF_alloc
    else:
        alloc = BF_alloc

    while 1:
        operate = input("请输入操作(1:申请，2:释放 -1:退出):")
        if operate == "1":
            task_id = int(input("请输入作业id:"))
            size = int(input("请输入空间大小:"))
            alloc(task_id, size)
        elif operate == "2":
            task_id = int(input("请输入作业id:"))
            free(task_id)
        else:
            exit(0)


def showList():
    tb = pt.PrettyTable()
    tb.field_names = ["起始地址", "结束地址", "空间大小", "状态", '编号']

    for i in range(len(blockList)):
        block = blockList[i]
        if block.state == 1:
            state = "已分配"
        else:
            state = "空闲"
        tb.add_row([block.start, block.end, block.length, state, block.id])

    print(tb)


# 分区
def FF_alloc(task_id, size):
    for i in range(len(blockList)):
        block = blockList[i]
        if block.state == 0 and block.length > size:
            newBlock = Block(block.start, block.start + size - 1, size, 1, task_id)
            freeBlock = Block(block.start + size, block.end, block.length - size, 0, 0)
            del blockList[i]
            blockList.insert(i, freeBlock)
            blockList.insert(i, newBlock)
            showList()
            return
        elif block.state == 0 and block.length == size:
            block.state = 1
            showList()
            return
    print("内存空间不足")


# 寻找最佳存放位置
def find_best_place(size):
    minIndex = -1  # 位置
    minSize = sys.maxsize  # 最小剩余空间
    for i in range(len(blockList)):
        # 空闲 且 剩余空间大于所需空间
        if blockList[i].state == 0 and 0 < blockList[i].length - size < minSize:
            minIndex = i
            minSize = blockList[i].length - size

    return [minIndex, minSize]


# 分区
def BF_alloc(task_id, size):
    [minIndex, minSize] = find_best_place(size)
    if minIndex == -1:
        print("内存空间不足")
        return

    block = blockList[minIndex]
    if minSize == 0:
        block.state = 1
        showList()
    else:
        newBlock = Block(block.start, block.start + size - 1, size, 1, task_id)
        freeBlock = Block(block.start + size, block.end, block.length - size, 0, 0)
        del blockList[minIndex]
        blockList.insert(minIndex, freeBlock)
        blockList.insert(minIndex, newBlock)
        showList()


def free(task_id):
    for i in range(len(blockList)):
        if blockList[i].id == task_id:
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

            showList()
            break


if __name__ == '__main__':
    # 初始化分区
    blockList = []
    init = Block(0, 639, 640, 0, 0)
    blockList.append(init)

    input_task()
