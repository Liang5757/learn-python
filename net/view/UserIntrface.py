import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import queue
import os
from scaner_port import *


class InitWindows(object):

    def __init__(self):
        self.btn_width = 20

        self.root = tk.Tk()
        self.root.geometry(
            f"780x330+{int(self.root.winfo_screenwidth() / 2) - 110}+{int(self.root.winfo_screenheight() / 2) - 180}")
        self.root.title("端口扫描器")
        self.data_tree = ttk.Treeview(self.root, show="headings")
        self.init_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def on_closing(self):
        if tk.messagebox.askokcancel("退出", "确认退出？"):
            # 退出 gui 直接结束进程, 防止程序继续执行消耗资源
            os.system('taskkill /f /im %s' % 'python.exe')
            self.root.destroy()

    def init_widgets(self):
        # All label
        lb_input_ip = tk.Label(self.root, text="请输入ip地址或ip地址段", anchor="center", width=self.btn_width)
        lb_input_port = tk.Label(self.root, text="请输入端口号或端口范围", anchor="center", width=self.btn_width)
        lb_ip1_title = tk.Label(self.root, text="下界", anchor="center")
        lb_ip2_title = tk.Label(self.root, text="上界", anchor="center")
        lb_port1_title = tk.Label(self.root, text="下界", anchor="center")
        lb_port2_title = tk.Label(self.root, text="上界", anchor="center")

        # All Entry box
        self.entry_input_ip1 = tk.Entry(self.root, width=self.btn_width + 1)
        self.entry_input_ip2 = tk.Entry(self.root, width=self.btn_width + 1)
        self.entry_input_port1 = tk.Entry(self.root, width=self.btn_width + 1)
        self.entry_input_port2 = tk.Entry(self.root, width=self.btn_width + 1)
        self.scan_btn = tk.Button(self.root, text="扫描", width=self.btn_width * 2, pady=10, command=self.get_)

        # ip地址输入区域
        lb_input_ip.place(x=15, y=20)
        lb_ip1_title.place(x=20, y=60)
        lb_ip2_title.place(x=20, y=100)
        self.entry_input_ip1.place(x=60, y=60)
        self.entry_input_ip2.place(x=60, y=100)

        # 端口输入区域
        lb_input_port.place(x=15, y=140)
        lb_port1_title.place(x=20, y=180)
        lb_port2_title.place(x=20, y=220)
        self.entry_input_port1.place(x=60, y=180)
        self.entry_input_port2.place(x=60, y=220)

        # 文件数据显示表格
        self.data_tree.place(x=250, y=20)
        # 定义列
        self.data_tree["columns"] = ("ip", "端口", "主机名", "开放端口", "端口类型", "服务名称")
        # 设置列属性，列不显示
        self.data_tree.column("ip", width=110)
        self.data_tree.column("端口", width=70)
        self.data_tree.column("主机名", width=120)
        self.data_tree.column("开放端口", width=60)
        self.data_tree.column("端口类型", width=60)
        self.data_tree.column("服务名称", width=80)
        # 设置表头
        self.data_tree.heading("ip", text="ip")
        self.data_tree.heading("端口", text="端口")
        self.data_tree.heading("主机名", text="主机名")
        self.data_tree.heading("开放端口", text="开放端口")
        self.data_tree.heading("端口类型", text="端口类型")
        self.data_tree.heading("服务名称", text="服务名称")
        # 开始扫描
        self.scan_btn.place(x=250, y=265)

    # 192.168.1.102
    # 1
    def get_(self):
        results = []
        try:
            ip1 = self.entry_input_ip1.get()
            ip2 = self.entry_input_ip2.get()
            port1 = self.entry_input_port1.get()
            port2 = self.entry_input_port2.get()

            if ip2 == "":
                ip2 = "255"

            if port2 == "":
                port2 = "65535"

            if int(port1) > int(port2):
                tk.messagebox.showinfo("Info", "输入非法")
                return
            if int(ip1.split('.')[-1]) > int(ip2.split('.')[-1]) or int(ip2.split('.')[-1]) > 255:
                tk.messagebox.showinfo("Info", "输入非法")
                return

            port_scanner = PortScanner()
            port_list = port_scanner.get_port_lists(int(port1), int(port2))
            ip_list = []

            for ip_last in range(int(ip1.split('.')[-1]), int(ip2.split('.')[-1])+1):
                ip_list.append('.'.join(ip1.split('.')[:-1])+"."+str(ip_last))

            for (index_y, ip) in enumerate(ip_list):
                thread_num = 100  # 线程数量
                port_queue = queue.Queue()
                threads = []  # 保存新线程

                for port in port_list:
                    port_queue.put(port)
                for t in range(thread_num):
                    threads.append(port_scanner.PortScan(port_queue, ip, results))
                # 启动线程
                for thread in threads:
                    thread.start()
                # 阻塞线程
                for thread in threads:
                    thread.join()

                # 显示结果
                for (index_x, result) in enumerate(results):
                    [ip, port, host_name, status, port_type, service_name] = result
                    self.data_tree.insert('', index_y*len(port_list) + index_x, values=(ip, port, host_name, status, port_type, service_name))

        except Exception:
            tk.messagebox.showinfo("Info", "输入非法")


if __name__ == '__main__':
    InitWindows()
