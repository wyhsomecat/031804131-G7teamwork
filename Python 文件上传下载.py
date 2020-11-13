#!/usr/bin/env python
# coding=utf-8

import paramiko
import sys

class SFTP():
    """
    实现ssh远程登陆，并且上传下载文件
    """

    def __init__(self, ip=None, filename=None, choose="-h"):
        self.ip = ip
        # 如果常用一个ip，可以设置默认ip
        if not self.ip:
            self.ip = "阿里云服务器ip"
        self.filename = filename
        self.choose = choose

        self.justice()

    def justice(self):
        # 判断用户需要的功能
        """
        根据参数，判断执行函数
        """
        if self.choose == "-d":
            self.do_it = self.download
        elif self.choose == "-u":
            self.do_it = self.upload
        elif self.choose == "-h":
            self.do_it = self.help
        else:
            self.do_it = self.help

    def start(self):
        # 执行
        self.do_it()

    def help(self):
        # 帮助文档
        print("\n", end="")
        print("参数:")
        print("-d[download]  下载文件")
        print("-u[upload]    上传文件")
        print("-h[help]      帮    助")
        print("\n", end="")
        print("格式:")
        print("python3 STFP.py [ip] [filename] [-u|-d|-h]")

    def connect(self):
        # 连接
        try:
            conn = paramiko.Transport((self.ip, 22))
        except Exception as e:
            print(e)
        else:
            # 用户名，用户密码
            self.name = input("用户名:")
            passwd = input("登陆密码:")
            try:
                # 尝试与远程服务器连接
                conn.connect(username = self.name, password = passwd)
                self.sftp_ob = paramiko.SFTPClient.from_transport(conn)
            except Exception as e:
                # 失败则打印原因
                print(e)
                return
            else:
                print("连接成功！")

    def download(self):
        self.connect()
        # print("正在下载..")
        self.sftp_ob.get("/home/"+self.name.lower()+"/download/"+self.filename, "D:/aliyun/download/"+self.filename)
        print("完成！")

    def upload(self):
        self.connect()
        # print("正在上传...")
        self.sftp_ob.put("D:/aliyun/upload/"+self.filename, "/home/"+self.name.lower()+"/upload/"+self.filename)
        print("完成！")


def main():
    try:
        sftp = SFTP(sys.argv[1], sys.argv[2], sys.argv[3])
    except:
        if "-h" in sys.argv:
            sftp = SFTP(choose=sys.argv[1])
        else:
            sftp = SFTP()

    sftp.start()

if __name__ == "__main__":
    main()
    #https://blog.csdn.net/qq_41359051/article/details/79965814