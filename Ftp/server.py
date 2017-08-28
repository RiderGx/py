# -*- coding: utf-8 -*-
import os
import sys
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
                    Ftp_user()

                else:
                    print('账号密码错误')
                    exit()

    def loca_sf(self):
        print(self.local)
        list = []
        for root, dirs, files in os.walk(self.local):
            if root != self.local:break
            for name in dirs:
                if name == self.name:continue
                else:
                    list.append(os.path.join(name))
                    print('\033[1;35;m%s \033[0m'%(os.path.join(name)))
            for name in files:
                list.append(os.path.join(name))
                print('\033[1;31;m%s \033[0m'%(os.path.join(name)))
        # while True:
        #     file_input = input("继续文件操作>>>>:").strip()
        #     if file_input == 'y' or file_input == 'Y':
        #         return Ftp_server.file_download_operation(self)# 文件操作权限
        #     else:
        #         print('输入错误，重新输入')


    def file_download_operation(self):
        file = input('输入要上传或者下载的文件')
        print('这是要拷贝的地址',self.local)
        print('这是要本地路径',self.local)

        # f1 = open('files', 'r', encoding='utf-8')
        # f2 = open('files.back', 'w', encoding='utf-8')
        #
        # files = f1.read()
        # f2.write(files)
        # f1.close()
        # f2.close()


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
        self.local = "%s\%s" % (os.getcwd(),self.name)
        Ftp_user.Ftp_user_chroice(self)


    def Ftp_user_chroice(self):
        print(self.local)
        user_chroice = input("输入>>>>>>:")
        if user_chroice == '1':
            return Ftp_server.loca_sf(self)
        elif user_chroice == '2':
            return Ftp_server.file_download_operation(self)
        elif 'cd' in user_chroice:
            return Ftp_user.path_modification(self,user_chroice)


    def path_modification(self,user_chroice):
        user_chroice = user_chroice.strip('cd'+'')
        self.local = self.local + os.

name = input('姓名:')
passwd = input('密码:')
user = Ftp_server(name,passwd)
user.User_Authentication()


111111111111111111111111