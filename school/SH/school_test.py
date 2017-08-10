# -*- coding: utf-8 -*-
import os
import json
class User_data(object):
    def __init__(self,name):
        self.name = name

    def User_Authentication(self):
        try:
            username =  open('%s\SH\student\%s.json'%(os.getcwd(),self.name), 'r', encoding='utf-8')
        except FileNotFoundError:
            return User_data.Student_registration(self)
        else:
            pass

    def Student_registration(self):
        profession = 'student'
        subject = []
        user_data= {'name':self.name,'prifession':profession,'subject':subject}
        return SchoolMember(user_data)

class SchoolMember(object): #学校模板
    def __init__(self,user_data):
        self.name = name
        self.user_data = user_data
        SchoolMember.student_chorice(self)

    def student_chorice(self):
        student_chorice = input('请输入你想学的科目>>>>>:')
        self.user_data['subject'].append(student_chorice)
        if student_chorice == 'go':
            print(self.user_data)

name = 'aa'
a = User_data(name)
a.User_Authentication()