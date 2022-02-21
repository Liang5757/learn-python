import tkinter as tk

#
app = tk.Tk()
app.title("你靓哥")
# 窗口大小('长x宽')
app.geometry('200x100')

var = tk.StringVar()
theLabel = tk.Label(app, textvariable=var, bg='green',
                    font=('Arial', 12), width=17, height=2)
theLabel.pack()

on_hit = False
def hit_me():
    global on_hit
    if on_hit:
        var.set('')
        on_hit = False
    else:
        var.set('你靓哥!')
        on_hit = True

button = tk.Button(app, text='hit me', width=15,
                   height=2, command=hit_me)
button.pack()


app.mainloop()
