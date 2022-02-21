#输出10到100之间的随机数
import random
randomnumber = [random.randint(10,100) for i in range(10)]
print("生成的随机数是：", randomnumber)

#生成商品价格打五折的列表，并生成大于5000元商品的列表
price = [1200, 5330, 2988, 6200, 1998, 8888]
sale = [int(x*0.5) for x in price]                  # sale列表打五折后构成列表
high_price = [x for x in price if x > 5000]         # sale列表中大于5000的元素构成列表
print("打五折后的价格：" ,sale, end = '')           # end = ''不换行
print()
print("价格高于5000：" , high_price)