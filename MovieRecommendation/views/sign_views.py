import pickle
from tkinter import messagebox

from views.main_view import *


# 登录界面
class LoginView(object):
    def __init__(self, master):
        self.window = master
        self.window.title('Welcome to movie recommendation')
        self.window.geometry('350x320')
        # 载入登入界面
        self.sign_page = tk.Frame(self.window)
        # 账户输入框文字
        self.var_user_name = tk.StringVar()
        # 密码输入框文字
        self.var_user_pw = tk.StringVar()
        self.image_file = tk.PhotoImage(file='welcome.png')
        self.creatView()
        # 作为显示密码的标记
        self.on_hit = False

    # 界面布局
    def creatView(self):
        # 登录界面
        self.sign_page.pack()
        # 嵌入图片
        canvas = tk.Canvas(self.sign_page, height=500, width=500)
        canvas.create_image(0, 0, anchor='nw', image=self.image_file)
        canvas.pack(side='top')
        # 登录标签
        tk.Label(self.sign_page, text='User name:').place(x=45, y=190)
        tk.Label(self.sign_page, text='Password:').place(x=46, y=230)
        # 显示给用户输入格式
        self.var_user_name.set('example@python.com')
        # 输入账户框
        entry_user_name = tk.Entry(self.sign_page, textvariable=self.var_user_name)
        entry_user_name.place(x=130, y=190)
        # 输入密码框
        entry_user_pw = tk.Entry(self.sign_page, textvariable=self.var_user_pw, show='*')
        entry_user_pw.place(x=130, y=230)
        # 登入注册按钮
        tk.Button(self.sign_page, text='Sign in', command=self.userSignIn).place(x=200, y=270)
        tk.Button(self.sign_page, text='Sign up', command=self.userSignUp).place(x=90, y=270)

        # 显示密码
        def show_pw():
            if self.on_hit:
                entry_user_pw.config(show='')
                self.on_hit = False
            else:
                entry_user_pw.config(show='*')
                self.on_hit = True
        # 显示密码按钮
        tk.Button(self.sign_page, text='show', command=show_pw).place(x=285, y=225)


    # 登入逻辑
    def userSignIn(self):
        # 获取输入框内的文字
        user_name = self.var_user_name.get()
        user_pw = self.var_user_pw.get()
        try:
            with open('user_info.pickle', 'rb') as user_file:
                user_info = pickle.load(user_file)
        except FileNotFoundError:
            with open('user_info.pickle', 'wb') as user_file:
                user_info = {'admin': 'admin'}
                pickle.dump(user_info, user_file)
        if user_name in user_info:
            if user_pw == user_info[user_name]:
                self.sign_page.destroy()
                MainView(self.window, user_name)
                # tk.messagebox.showinfo(title='Welcome', message='How are you? ' + user_name)
            else:
                tk.messagebox.showerror(message='Error, your password is wrong')
        else:
            is_sign_up = tk.messagebox.askyesno(title='Error', message='you have not sign up yet!')
            if is_sign_up:
                self.userSignUp()

    # 注册界面
    def userSignUp(self):
        # 注册逻辑
        def sign_to_user_info():
            np = new_pw.get()
            npf = cf_new_pw.get()
            nn = new_name.get()
            with open('user_info.pickle', 'rb') as user_file:
                exist_user_info = pickle.load(user_file)
            if np != npf:
                tk.messagebox.showerror(title='Error', message='Password and confirm password must be the same!')
            elif nn in exist_user_info:
                tk.messagebox.showerror(title='Error', message='The user has already signed up!')
            else:
                exist_user_info[nn] = np
                with open('user_info.pickle', 'wb') as user_file:
                    pickle.dump(exist_user_info, user_file)
                tk.messagebox.showinfo(title='Welcome', message='You have successfully signed up!')
                window_sign_up.destroy()

        window_sign_up = tk.Toplevel(self.sign_page)
        window_sign_up.geometry('350x200')
        window_sign_up.title('Sign up window')

        new_name = tk.StringVar()
        new_name.set('example@python.com')
        tk.Label(window_sign_up, text='User name:').place(x=10, y=10)
        tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)

        new_pw = tk.StringVar()
        tk.Label(window_sign_up, text='Password:').place(x=10, y=50)
        tk.Entry(window_sign_up, textvariable=new_pw, show='*').place(x=150, y=50)

        cf_new_pw = tk.StringVar()
        tk.Label(window_sign_up, text='Confirm Password:').place(x=10, y=90)
        tk.Entry(window_sign_up, textvariable=cf_new_pw, show='*').place(x=150, y=90)

        tk.Button(window_sign_up, text='sign up', command=sign_to_user_info).place(x=150, y=130)

root = tk.Tk()
view = LoginView(root)
root.mainloop()


