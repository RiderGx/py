# -*- coding: utf-8 -*-
import os
import json


class Ftp_server(object):
    local = os.getcwd()#本地路径

    def __init__(self,name,passwd):
        self.name = name
        self.passwd = passwd

    def User_Authentication(self):
        '''用户认证'''
        if self.name == 'root' and self.passwd == 'root':
            Ftp_root()
        else:
            try:
                user_ =  open(r"%s/user/%s.json"%(os.getcwd(),self.name), 'r')
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
        '''本地文件打印'''
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
        return Ftp_user.Ftp_user_chroice(self)



    def file_operation(self,user_chroice):
        '''文件操作'''
        source_path = ''
        destination_path = ''
        if user_chroice[0] == 'copy':
            user_chroice.remove('copy')
            source_path = self.local
            destination_path = local
        elif user_chroice[0] == 'upload':
            user_chroice.remove('upload')
            source_path = local
            destination_path = self.local
        try:
            file_operation = ''.join(user_chroice)
            file_1 = open("%s/%s"%(source_path,file_operation), 'r', encoding='utf-8')
            file_2 = open('%s/%s'%(destination_path,file_operation), 'w', encoding='utf-8')
        except FileNotFoundError:
            print('找不到该文件')
        except PermissionError:
            print('这是一个文件夹，无法被复制')
        else:
             files = file_1.read()
             file_2.write(files)
             file_2.flush()

        return Ftp_user.Ftp_user_chroice(self)


    def file_list(self,user_chroice):
        '''本地文件查看'''
        user_chroice = ''.join(user_chroice)

        try:
            file_read =  open('%s/%s'%(self.local,user_chroice),'r',encoding='utf-8')
        except FileNotFoundError:
            print('找不到文件')
        else:
            file = file_read.read()
            print(file)
        return Ftp_user.Ftp_user_chroice(self)

    def user_mkdir(self,user_chroice):
        '''用户创建文件'''
        mkdir_name = ''.join(user_chroice)
        list = ['copy', 'upload', 'cd', 'ls', 'mkdir', 'pwd', 'cat']
        if len(user_chroice) == 0:
            print('输入文件夹名字')
        elif mkdir_name in list:
            print('不能使用系统名创建文件夹')
        else:
             os.mkdir(mkdir_name)
        return Ftp_user.Ftp_user_chroice(self)


class Ftp_user(Ftp_server):
    def __init__(self):
        super(Ftp_user,self).__init__(name,passwd)
        self.local = r"%s/%s" % (local,self.name)
        os.chdir(self.local)
        Ftp_user.Ftp_user_chroice(self)

    def Ftp_user_chroice(self):
        '''用户操作'''
        user_chroice = input("输入>>>>>>:")
        user_chroice = user_chroice.split()
        if user_chroice[0] == 'ls':
            return Ftp_server.loca_sf(self)
        elif user_chroice[0] == 'cd':
            user_chroice.remove('cd')
            return Ftp_user.path_modify(self,user_chroice)
        elif user_chroice[0] == 'copy':
            return Ftp_server.file_operation(self,user_chroice)
        elif user_chroice[0] == 'upload':
            return Ftp_server.file_operation(self, user_chroice)
        elif user_chroice[0]=='cat':
            user_chroice.remove('cat')
            return Ftp_server.file_list(self,user_chroice)
        elif user_chroice[0] == 'pwd':
            print('当前目录：', os.getcwd())
        elif user_chroice[0] == 'mkdir':
            user_chroice.remove('mkdir')
            return Ftp_server.user_mkdir(self,user_chroice)
        elif user_chroice[0] == 'q':
            exit()
        return Ftp_user.Ftp_user_chroice(self)


    def path_modify(self,user_chroice):
        '''路径修改'''
        user_chroice = ''.join(user_chroice)
        local_path = r"%s/%s" % (self.local,user_chroice)
        initial_path = r"%s/%s" % (local,self.name)
        if user_chroice == '..':
            if self.local == initial_path:
                print('这是根目录')
            else:
                os.chdir(self.local)
                os.chdir(os.pardir)
                self.local = os.getcwd()
        elif os.path.isdir(local_path) == True:
            os.chdir(local_path)
            self.local = os.getcwd()
        else:
            print('这不是一个文件夹')
        return Ftp_user.Ftp_user_chroice(self)



class Ftp_root(Ftp_server):
    def __init__(self):
        super(Ftp_root,self).__init__(name,passwd)
        return Ftp_root.root_user(self)

    def root_user(self):
        root_chroice = input('文件操作选择1，注册账号选2：')
        if root_chroice == '1':
            Ftp_user()
        elif root_chroice == '2':
            return Ftp_root.print_self(self)
        else:
            print('输入错误')
            return Ftp_root.root_user(self)



    def print_self(self):
        '''注册新用户'''
        username = input('输入用户>>>:').strip()
        path = r"%s/user/%s.json" % (os.getcwd(), username)
        locasf = r"/Ftp/%s" % (username)
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


name = input('姓名:')
passwd = input('密码:')
local = os.getcwd()
user = Ftp_server(name,passwd)
user.User_Authentication()