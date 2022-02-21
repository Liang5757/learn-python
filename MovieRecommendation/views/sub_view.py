import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
import pickle

#
class UserView(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master
        self.itemName = tk.StringVar()
        self.importPrice = tk.StringVar()
        self.sellPrice = tk.StringVar()
        self.deductPrice = tk.StringVar()
        self.createPage()

    def createPage(self):
        tk.Label(self).grid(row=0, pady=10)
        tk.Label(self, text='待填充 ').grid(row=1, pady=10)

# 电影分类搜索界面
class SearchView(tk.Frame):  # 继承Frame类
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.itemName = tk.StringVar()
        self.createPage()

    # 布局
    def createPage(self):
        tk.Label(self, text='查询界面').pack()

# 电影详情界面
class MovieDetailView(tk.Frame):  # 继承Frame类
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()

    def createPage(self):
        tk.Label(self, text='详情界面').pack()

# 用户个人界面
on_hit = False
class UserInfoView(tk.Frame):  # 继承Frame类
    def __init__(self, master=None, user=None):
        tk.Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.image_file = Image.open('Head_portrait.jpg')
        self.user_name = user
        self.createPage()
        # 作为显示密码的标记
        self.on_hit = False

    def createPage(self):
        # 嵌入图片
        canvas = tk.Canvas(self, height=800, width=800)
        # 缩放图片
        image_resized = self.image_file.resize((150, 150), Image.ANTIALIAS)
        self.image_file = ImageTk.PhotoImage(image_resized)
        canvas.create_image(520, 100, anchor='nw', image=self.image_file)
        canvas.pack(side='top')
        tk.Label(self, text='个人信息').place(x=100, y=50)
        tk.Label(self, text='用户名：').place(x=100, y=80)
        tk.Label(self, text=self.user_name).place(x=150, y=80)
        tk.Label(self, text='密码：就不告诉你').place(x=100, y=110)
        tk.Button(self, text='修改密码', command=self.change_pw).place(x=100, y=150)

    def change_pw(self):
        # 储存信息
        def change_user_pw():
            np = new_pw.get()
            cp = com_pw.get()
            with open('user_info.pickle', 'rb') as user_file:
                exist_user_info = pickle.load(user_file)
            if np != cp:
                tk.messagebox.showerror(title='Error', message='Password and confirm password must be the same!')
            else:
                exist_user_info[self.user_name] = np
                with open('user_info.pickle', 'wb') as user_file:
                    pickle.dump(exist_user_info, user_file)
                tk.messagebox.showinfo(title='Welcome', message='You have successfully changed your password!')
                window_change_pw.destroy()

        window_change_pw = tk.Toplevel(self.root)
        window_change_pw.geometry('380x200')
        window_change_pw.title('change password window')

        new_pw = tk.StringVar()
        tk.Label(window_change_pw, text='New Password:').place(x=10, y=50)
        new_pw_entry = tk.Entry(window_change_pw, textvariable=new_pw, show='*')
        new_pw_entry.place(x=150, y=50)

        com_pw = tk.StringVar()
        tk.Label(window_change_pw, text='Confirm Password:').place(x=10, y=90)
        tk.Entry(window_change_pw, textvariable=com_pw, show='*').place(x=150, y=90)

        # 显示密码
        def show_pw():
            if self.on_hit:
                new_pw_entry.config(show='')
                self.on_hit = False
            else:
                new_pw_entry.config(show='*')
                self.on_hit = True

        tk.Button(window_change_pw, text='确认', command=change_user_pw).place(x=150, y=130)
        # 显示密码按钮
        tk.Button(window_change_pw, text='显示密码', command=show_pw).place(x=308, y=47)
