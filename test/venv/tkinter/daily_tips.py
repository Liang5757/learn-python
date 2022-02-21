from tkinter import *
# 导入tkinter模块的所有内容
import datetime

root = Tk()

#定义一个列表
mot = ["今天星期一：\n坚持下去不是因为我很坚强，而是因为我别无选择。",
       "今天星期二：\n含泪播种的人一定能笑着收获。",
       "今天星期三：\n做对的事情比把事情做对重要。",
       "今天星期四：\n越努力，越幸福。",
       "今天星期五：\n不要等到明天，明天太遥远，今天就行动。",
       "今天星期六：\n求知若饥，虚心若愚。",
       "今天星期日：\n成功将属于哪些从不说“不可能”的人"]
day = datetime.datetime.now().weekday()          #获得当前日期

# 创建一个文本Label对象
textLabel = Label(root,   # 将内容绑定在  root 初始框上面
                  text = mot[day],
                  justify = LEFT, # 用于 指明文本的 位置
                  padx = 10)        #   限制 文本的 位置 , padx 是 x轴的意思 .
textLabel.pack(side=LEFT)   # 致命 textlabel 在初识框 中的位置

# 创建一个图像Label对象
# 用PhotoImage实例化一个图片对象（支持gif格式的图片）
photo = PhotoImage(file = "努力.png")
imgLabel = Label(root, image=photo)  # 绑定在初始旷上面
imgLabel.pack(side = RIGHT)  # 指明 图片位置

mainloop()
