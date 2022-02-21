import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# show参数：所有输入变成*号
entry = tk.Entry(window, show='*')
entry.pack()

def insert_point():
    var = entry.get()
    t.insert('insert', var)

def insert_end():
    var = entry.get()
    t.insert('end', var)

b1 = tk.Button(window, text='insert point', width=15,
               height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end', width=15,
               height=2, command=insert_end)
b2.pack()

t = tk.Text(window, height=2)
t.pack()

window.mainloop()
