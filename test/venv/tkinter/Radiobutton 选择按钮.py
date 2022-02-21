import tkinter as tk

window = tk.Tk()
window.title('选择你喜欢的话')
window.geometry('200x200')

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

def print_selection():
    # 重新配置控件属性
    l.config(text='your have selected' + var.get())


var = tk.StringVar()
# 当选择此选项时，把value参数的值赋给var
r1 = tk.Radiobutton(window, text='Option A',
                    variable=var, value='A',
                    command=print_selection)
r1.pack()

r2 = tk.Radiobutton(window, text='Option B',
                    variable=var, value='B',
                    command=print_selection)
r2.pack()

r3 = tk.Radiobutton(window, text='Option C',
                    variable=var, value='C',
                    command=print_selection)
r3.pack()

window.mainloop()
