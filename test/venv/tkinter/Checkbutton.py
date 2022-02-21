import tkinter as tk

window = tk.Tk()
window.title('选择你喜欢的话')
window.geometry('200x200')

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()


def print_selection():
    if var1.get() == 1 and var2.get() == 0:
        l.config(text='I love only Python')
    elif var1.get() == 0 and var2.get() == 1:
        l.config(text='I love only C++')
    elif var1.get() == 0 and var2.get() == 0:
        l.config(text="I don't love either")
    else:
        l.config(text='I love both')

var1 = tk.IntVar()
# onvalue=1表示点选后var值为1, offvalue=0不选var值为0
c1 = tk.Checkbutton(window, text='Python', variable=var1,
                    onvalue=1, offvalue=0, command=print_selection)
c1.pack()

var2 = tk.IntVar()
c2 = tk.Checkbutton(window, text='C++', variable=var2,
                    onvalue=1, offvalue=0, command=print_selection)
c2.pack()

window.mainloop()
