from views.sub_view import *
import tkinter as tk

class MainView(object):
    def __init__(self, master, user_name):
        self.root = master
        self.root.geometry('800x600')
        self.mainview = UserView(self.root)
        self.searchview = SearchView(self.root)
        self.moviedetailview = MovieDetailView(self.root)
        self.userinfoview = UserInfoView(self.root, user_name)
        self.creatView()


    # 布局
    def creatView(self):
        # 默认显示主菜单
        self.mainview.pack()
        menubar = tk.Menu(self.root)
        menubar.add_command(label='主界面', command=self.mainView)
        menubar.add_command(label='查询', command=self.searchView)
        menubar.add_command(label='详情', command=self.movieDetailView)
        menubar.add_command(label='个人信息', command=self.userView)
        self.root['menu'] = menubar  # 设置菜单栏

    def mainView(self):
        self.mainview.pack()
        self.searchview.pack_forget()
        self.moviedetailview.pack_forget()
        self.userinfoview.pack_forget()

    def searchView(self):
        self.mainview.pack_forget()
        self.searchview.pack()
        self.moviedetailview.pack_forget()
        self.userinfoview.pack_forget()

    def movieDetailView(self):
        self.mainview.pack_forget()
        self.searchview.pack_forget()
        self.moviedetailview.pack()
        self.userinfoview.pack_forget()

    def userView(self):
        self.mainview.pack_forget()
        self.searchview.pack_forget()
        self.moviedetailview.pack_forget()
        self.userinfoview.pack()