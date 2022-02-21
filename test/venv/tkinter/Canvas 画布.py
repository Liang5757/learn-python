import tkinter as tk

window = tk.Tk()
window.title('选择你喜欢的话')
window.geometry('500x500')

canvas = tk.Canvas(window, bg='blue', height=100, width=200)
image_file = tk.PhotoImage(file='ins.png')
image = canvas.create_image(10, 10, anchor='nw', image=image_file)

x0, y0, x1, y1 = 50, 50, 80, 80
# 画线
line = canvas.create_line(x0, y0, x1, y1)
# 画圆
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
# 扇形
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)
# 矩形
rect = canvas.create_rectangle(100, 30, 120, 50)

# 移动正方形
def moveit():
    # 负数则向上
    canvas.move(rect, 0, -2)
# 按钮
b = tk.Button(window, text='move', command=moveit).pack()

canvas.pack()

window.mainloop()
