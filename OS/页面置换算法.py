import random


# 内存块定义
class Block(object):
    def __init__(self, numPage=-1, accessed=0):
        self.numPage = numPage  # 页号
        self.accessed = accessed  # 访问情况，数值表示多久未被访问


def initData(block):
    for i in range(size):
        block.append(Block(numPage=-1, accessed=0))


# 查找物理块中是否有该页面
def findPage(block, curpage):
    for i in range(size):
        if block[i].numPage == curpage:
            return i
    return -1


# 查找置换的页号
def findExchange(block):
    pos = 0
    for i in range(size):
        if block[i].accessed > block[pos].accessed:
            pos = i
    return pos


# 生成随机指令序列
def randomOrder():
    flag = 0
    count = random.randint(0, orderNum - 1)
    num = 0
    standard = []
    while num < orderNum:
        if count not in standard:
            standard.append(count)
            orderList.append(count)
            num = num + 1
        else:
            count = random.randint(0, orderNum - 1)

        if flag % 2 == 0:
            count = count + 1
            count = count % orderNum
        if flag == 1:
            if count - 1 > 0:
                count = random.randint(0, count - 1)
            else:
                count = 0
        if flag == 3:
            if count + 1 < orderNum:
                count = random.randint(count + 1, orderNum - 1)
            else:
                count = orderNum
        flag = flag + 1
        flag = flag % 4


# 找到空闲空间
def findSpace(block):
    for i in range(size):
        if block[i].numPage == -1:
            return i
    return -1


def printBlock(block):
    printList = []
    for i in range(size):
        if block[i].numPage != -1:
            printList.append(block[i].numPage)
    print(printList)


def FIFO(block, pageFaultNum):
    curpage = -1
    exchange = -1
    for i in range(orderNum):
        count = orderList[i]
        curpage = int(count / 10)   # 所在页数
        exsist = findPage(block, curpage)  # 该页是否存在于内存中
        if exsist == -1:
            space = findSpace(block)    # 寻找置换位置
            if space == -1:
                block.pop()
                block.append(Block(numPage=curpage, accessed=0))
            else:
                block[space].numPage = curpage
            pageFaultNum = pageFaultNum + 1
            printBlock(block)
        else:
            print("指令已在内存，页号为", curpage)
        # 所有内存块时间加一
        for j in range(size):
            block[j].accessed += 1
    print("缺页次数为：", pageFaultNum)
    v = pageFaultNum / 320.0 * 100
    print("缺页率为：", v, "%")


def LRU(block, pageFaultNum):
    curpage = -1
    exchange = -1
    for i in range(orderNum):
        count = orderList[i]
        curpage = int(count / 10)   # 所在页数
        exsist = findPage(block, curpage)  # 该页是否存在于内存中
        if exsist == -1:
            space = findSpace(block)    # 寻找置换位置
            if space == -1:
                exchange = findExchange(block)
                block[exchange].numPage = curpage
                block[exchange].accessed = 0
            else:
                block[space].numPage = curpage
                block[space].accessed = 0
            pageFaultNum = pageFaultNum + 1
            printBlock(block)
        else:
            block[exsist].accessed = 0
            print("指令已在内存，页号为", curpage)
        # 所有内存块时间加一
        for j in range(size):
            block[j].accessed += 1
    print("缺页次数为：", pageFaultNum)
    v = pageFaultNum / 320.0 * 100
    print("缺页率为：", v, "%")


def OPT(block, pageFaultNum):
    curpage = -1
    exchange = -1
    for i in range(orderNum):
        count = orderList[i]
        curpage = int(count / 10)
        exsist = findPage(block, curpage)
        if exsist == -1:
            space = findSpace(block)
            if space == -1:
                for h in range(size):
                    for k in range(i, 320):
                        if block[h].numPage != orderList[k] / 10:
                            block[h].accessed = 1000
                        else:
                            block[h].accessed = k
                            break
                exchange = findExchange(block)
                block[exchange].numPage = curpage
            else:
                block[space].numPage = curpage
            pageFaultNum = pageFaultNum + 1
            printBlock(block)
        else:
            print("指令已在内存，页号为", curpage)
    print("缺页次数为：", pageFaultNum)
    v = pageFaultNum / 320.0 * 100
    print("缺页率为：", v, "%")


if __name__ == '__main__':
    count = 0  # 记录指令的序号
    pageFaultNum = 0  # 缺页数目
    size = 6  # 内存块数目
    blockList = []  # 内存块
    orderList = []
    orderNum = 320

    randomOrder()
    initData(blockList)
    while 1:
        choice = int(input("输入1运行FIFO，输入2运行LRU，输入3运行OPT："))
        if choice == 1:
            FIFO(blockList, pageFaultNum)
        elif choice == 2:
            LRU(blockList, pageFaultNum)
        elif choice == 3:
            OPT(blockList, pageFaultNum)
