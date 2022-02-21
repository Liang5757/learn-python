import tkinter as tk

window = tk.Tk()
window.geometry('200x200')

for i in range(4):
    for j in range(3):
        tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)

# anchor='nw'中nw代表northwest
tk.Label(window, text=1).place(x=100, y=100, anchor='nw')

window.mainloop()
