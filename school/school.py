# -*- coding: utf-8 -*-
import json
import os

class User_data(object):
    def __init__(self,name):
        self.name = name

    def User_Authentication(self):
        if self.name == 'root':
            return User_data.Teacher_registration(self)
        try:
            username =  open('%s\SH\student\%s.json'%(os.getcwd(),self.name), 'r', encoding='utf-8')
        except FileNotFoundError:
            return User_data.Student_registration(self)
        else:
            pass

    def Teacher_registration(self):
        '''初始老师'''
        teacher_name = input('输入教师姓名>>>>>>:').strip()
        profession = 'teacher'
        subject = []
        user_data = {'name': teacher_name, 'prifession': profession, 'subject': subject}
        SchoolMember(user_data)

    def Student_registration(self):
        '''初始学生'''
        profession = 'student'
        subject = []
        user_data= {'name':self.name,'prifession':profession,'subject':subject}
        SchoolMember(user_data)

class SchoolMember(object): #学校模板
    def __init__(self,user_data):
        self.name = user_data['name']
        self.prifession = user_data['prifession']
        self.subject = user_data['subject']
        self.user_data = user_data
        SchoolMember.user_chorice(self)

    def user_chorice(self):
        '''选择学科，通过学科选择学校'''
        user_chorice_data = input('请输入科目>>>>>:').strip()
        self.subject.append(user_chorice_data)
        if user_chorice_data == 'linux' or user_chorice_data == 'python':
            School_bj.tell(self)
        elif user_chorice_data == 'go':
            School_sh.School_list(self)
        else:
            print('学科输入错误')

    def creat_class(self,add):
        with open('class_number','r',encoding='utf-8') as class_list_number:
            class_list_number = class_list_number.read()
            class_name =  self.course + '-' + class_list_number + '班'
            class_personnel = {'teacher': '','student':[]}
            with open('%s\%s\class\%s.json'%(os.getcwd(),add,class_name) , 'w', encoding='utf-8') as class_name_file:
                json.dump(class_personnel,class_name_file)
            class_list_number = int(class_list_number)
            class_list_number += 1
            class_list_number = str(class_list_number)
            with open('class_number', 'w', encoding='utf-8') as new_class_list_number:
                new_class_list_number.write(class_list_number)

    def class_list_add(self,add):
        path = '%s\%s\class'%(os.getcwd(),add)
        list = []
        for root, dirs, files in os.walk(path):
            for i in files:
                list.append(i)
        for index, item in enumerate(list):
            print(index, item)
        user_choice = int(input("选择班级加入班主任>>>:"))
        class_list = list[user_choice]
        print(class_list)
        with open('%s\%s\%s'%(path,add,class_list),'r')as class_list_f_r:
            class_list_name = json.load(class_list_f_r)
            class_list_name['teacher'] = self.name
            with open('%s\%s' % (path, class_list), 'w')as class_list_f_w:
                json.dump(class_list_name,class_list_f_w)


class School_bj(SchoolMember):
    '''定义了北京的分校'''
    def __init__(self,add):
        super(School_bj,self).__init__(name,course)
        self.add = add

    def tell(self):
        print('%s 老师在北京任课，教%s'%(self.name,self.course))


class School_sh(SchoolMember):
    '''定义了上海的分校'''
    def __init__(self):
        super(School_sh,self).__init__(name,prifession,subject,user_data)

    def School_list(self):
        if self.prifession == 'teacher':
            School_sh_list = input('选择查看')
            if School_sh_list == 'a':
                return School_sh.creat_class(self,'SH')
            elif School_sh_list == 'b':
                return School_sh.class_list_add(self,'SH')
            else:
                print(self.user_data)


name = 'root'
a = User_data(name)
a.User_Authentication()