import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

def hit_me():
    # 显示信息
    # tk.messagebox.showinfo(title='Hi', message='hahahahaha')
    # 显示警告，程序可以继续
    # tk.messagebox.showwarning(title='Hi', message='nonono')
    # 显示错误，程序无法进行
    # tk.messagebox.showerror(title='Hi', message='No!!never')
    # return 'yes', 'no'
    # print(tk.messagebox.askquestion(title='Hi', message='hahahaha'))
    print(tk.messagebox.askyesno(title='Hi', message='hahaha'))

tk.Button(window, text='hit me', command=hit_me).pack()

window.mainloop()
