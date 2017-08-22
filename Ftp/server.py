# -*- coding: utf-8 -*-
import os
import json




class Ftp_server(object):
    def __init__(self,name,passwd):
        self.name = name
        self.passwd = passwd

    def User_Authentication(self):
        if self.name == 'root' and self.passwd == 'root':
            Ftp_root()
        else:
            pass #跳到用户模式

class Ftp_root(Ftp_server):
    def __init__(self):
        super(Ftp_root,self).__init__(name,passwd)
        locasf = r"\%s\%s"%(os.getcwd(),self.name)
        self.locasf = locasf
        return Ftp_root.print_self(self)

    def print_self(self):
        print(self.locasf)
        # username = input('新的姓名')
        # self.name = username
        # os.mkdir(self.name)



name = input('姓名:')
passwd = input('密码:')
user = Ftp_server(name,passwd)
user.User_Authentication()