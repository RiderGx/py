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
            try:
                user_ =  open("%s\\user\%s.json"%(os.getcwd(),self.name), 'r')
            except FileNotFoundError:
                print('用户名不存在')
            else:
                user_data = json.load(user_)
                if self.name == user_data['username'] and self.passwd == user_data['password']:
                    return Ftp_user()
                    return user_data

                else:
                    print('账号密码错误')
                    exit()

class Ftp_root(Ftp_server):
    def __init__(self):
        super(Ftp_root,self).__init__(name,passwd)
        return Ftp_root.print_self(self)

    def print_self(self):
        username = input('输入用户>>>:').strip()
        path = "%s\\user\%s.json" % (os.getcwd(), username)
        locasf = r"\Ftp\%s" % (username)
        self.locasf = locasf
        if os.path.isfile(path) == 'True':
            print('用户存在')
        else:
            passwd = input('输入用户密码>>>：').strip()
            self.name = username
            user_dict = {"username":self.name,"password":passwd,"locasf":[locasf]}
            os.mkdir(self.name)
            with open(path,'w',encoding='utf-8') as user_w:
                json.dump(user_dict,user_w)
                exit()

class Ftp_user(Ftp_server):
    def __init__(self):
        super(Ftp_user,self).__init__(name,passwd)
        self.user_data = user_data


name = input('姓名:')
passwd = input('密码:')
user = Ftp_server(name,passwd)
user.User_Authentication()