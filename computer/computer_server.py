# -*- coding: utf-8 -*-
import multiprocessing,threading,os


def login(username,password):
    if username == 'root' and password == 'root':
        return root_option()

def root_option():
    root_operation_option = input('输入操作命令：>>>>>>').split()
    if root_operation_option[0] == 'cd':
        a = threading.Thread(target=computer_option, )
        a.start()
def user_option():
    pass


def computer_option():
     root_process = threading.Thread(target=computer_pwd, )
     root_process.start()


def computer_pwd():
    print(os.getcwd())
    return root_option()


if __name__ == '__main__':
    username = input('用户名：').strip()
    password = input('密码:').strip()
    login(username,password)