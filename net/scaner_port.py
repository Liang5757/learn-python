# !/usr/bin/env python3
# -*-coding:utf-8-*-

import socket
import threading


class PortScanner(object):
    class PortScan(threading.Thread):
        def __init__(self, port_queue, ip, result):
            threading.Thread.__init__(self)
            self.__port_queue = port_queue
            self.__ip = ip
            self.__timeout = 3
            self.result = result

        def get_result(self):
            try:
                return self.result
            except Exception:
                return None

        def run(self):
            """
            多线程实际调用的方法，如果端口队列不为空，循环执行
            """
            while True:
                if self.__port_queue.empty():
                    break

                port = self.__port_queue.get(timeout=0.5)
                ip = self.__ip

                status = self.get_port_Status(ip, port)
                host_name = self.get_host_name()

                service = self.get_service_name(port)

                if not service:
                    port_type = ""
                    service_name = ""
                else:
                    [port_type, service_name] = service

                self.result.append([ip, port, host_name, status, port_type, service_name])

        def get_port_Status(self, ip, port):
            """
            获取端口状态 返回str
            """
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(self.__timeout)
                result_code = s.connect_ex((ip, port))  # 开放放回0
                if result_code == 0:
                    return "开启"
                else:
                    return "关闭"
            except Exception as e:
                print(e)
                return "关闭"
            finally:
                s.close()

        @staticmethod
        def get_service_name(port):
            """
            获取服务名 返回[端口协议，服务名]
            """
            port_type = 'tcp'
            port_type2 = 'udp'
            try:
                return [port_type, socket.getservbyport(port, port_type)]
            except Exception:
                try:
                    return [port_type2, socket.getservbyport(port, port_type2)]
                except Exception:
                    return ""

        @staticmethod
        def get_host_name():
            """
            获取设备主机名 返回str
            """
            try:
                return socket.gethostname()
            except Exception as e:
                return ""



    @staticmethod
    def get_port_lists(start_port=1, end_port=65535):
        """
        获取扫描的端口list，top == None, start_port和end_port有效，top取值为50,100，1000分为为前top端口，当top == None时，并且端口号无效返回[1-65535]
        """
        if start_port >= 1 and end_port <= 65535 and start_port <= end_port:
            return list(range(start_port, end_port + 1))
        else:
            return list(range(1, 65535 + 1))