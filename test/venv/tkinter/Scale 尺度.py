import tkinter as tk

window = tk.Tk()
window.title('选择你喜欢的话')
window.geometry('200x200')

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

def print_selection(v):
    # 重新配置控件属性
    l.config(text='your have selected ' + v)

# showvalue=1则显示当前值
# resolution=0.01则保留两位小数
# orient=tk.HORIZONTAL横向显示滑动条
# tickinterval=3间隔为3显示值在滑动条下方
s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
             length=200, showvalue=0, tickinterval=3, resolution=0.01, command=print_selection)
s.pack()

window.mainloop()


