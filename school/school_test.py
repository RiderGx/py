import json
import os

class User_data(object):
    def __init__(self,name):
        self.name = name

    def User_Authentication(self):
        if self.name == 'root':
            return User_data.Teacher_registration(self)
        else:
            try:
                username =  open("%s\\user_database\%s.json"%(os.getcwd(),self.name), 'r')
            except FileNotFoundError:
                return User_data.Student_registration(self)
            else:
                user_data = json.load(username)
                password = input('输入密码>>>>>:').strip()
                if self.name == user_data['name'] and password == user_data['password']:
                    # SchoolMember(user_data)
                    print('正在登录')
                else:
                    print('账号密码错误')

    def Teacher_registration(self):
        '''初始老师'''
        while True:
            teacher_name = input('输入教师姓名>>>>>>:').strip()
            pasth = ("%s\\user_database\%s.json"%(os.getcwd(),teacher_name))
            if os.path.exists(pasth) == True:
                print('账号存在')
            else:
                password = input('输入密码>>>>>:').strip()
                profession = 'teacher'
                subject = ''
                user_data = {'name': teacher_name, 'password':password,'profession': profession, 'subject': subject,'location':''}
                SchoolMember(user_data)

    def Student_registration(self):
        '''初始学生'''
        password = input('输入密码>>>>>:').strip()
        profession = 'student'
        subject = {}
        user_data= {'name':self.name,'password':password,'profession':profession,'subject':subject,'location':''}
        SchoolMember(user_data)

name = input('请输入你的大名>>>>>>:').strip()
a = User_data(name)
a.User_Authentication()