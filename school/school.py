# -*- coding: utf-8 -*-
import json
import os
class SchoolMember(object): #学校模板
    def __init__(self,name,school_class,course):
        self.name = name
        self.course = course
        self.school_class = school_class
    def teaching(self):
        if self.course == 'linux' or self.course == 'python':
            School_bj.tell(self)
        if self.course == 'go':
            School_sh.School_list(self)
        else:
            print('输入错误')
    # def enroll(self):
    #     '''注册'''
    #     print('new school number [%s]'% self.name)
    #     SchoolMember.number += 1

    # def tell(self):
    #     print('-----info---:%s' % self.name)
    #     for k,v in self.__dict__.items():
    #         print('\t',k,v)

class School_bj(SchoolMember):
    '''定义了北京的分校'''
    def __init__(self,add):
        super(School_bj,self).__init__(name,course)
        self.add = add

    def tell(self):
        print('%s 老师在北京任课，教%s'%(self.name,self.course))


    # def open_branch(self,addr):
    #     print('开分校在[%s]'%addr)



class School_sh(SchoolMember):
    '''定义了上海的分校'''

    def __init__(self):
        super(School_bj,self).__init__(name,school_class,course)


    def School_list(self):
        School_sh_list = input('选择查看')
        if School_sh_list == 'a':
            return School_sh.creat_class(self)
        elif School_sh_list == 'b':
            return School_sh.class_list_add(self)



    def creat_class(self):
        with open('class_number','r',encoding='utf-8') as class_list_number:
            class_list_number = class_list_number.read()
            class_name =  'go' + '-' + class_list_number + '班'
            class_personnel = {'teacher': '','student':[]}
            with open('%s\SH\%s.json'%(os.getcwd(),class_name) , 'w', encoding='utf-8') as class_name_file:
                json.dump(class_personnel,class_name_file)
            class_list_number = int(class_list_number)
            class_list_number += 1
            class_list_number = str(class_list_number)
            with open('class_number', 'w', encoding='utf-8') as new_class_list_number:
                new_class_list_number.write(class_list_number)

    def class_list_add(self):
        path = '%s\SH'%(os.getcwd())
        list = []
        for root, dirs, files in os.walk(path):
            for i in files:
                list.append(i)
        for index, item in enumerate(list):
            print(index, item)
        user_choice = int(input("选择班级加入班主任>>>:"))
        class_list = list[user_choice]
        print(class_list)
        with open('%s\%s'%(path,class_list),'w')as class_list_f:
            class_list_name = json.load(class_list_f)
            class_list_name['teacher'] = self.name
            json.dump(class_list_name,class_list_f)



name = 'a'
course = input('输入教学学科').strip()
school_class = ''


t1 = SchoolMember(name,school_class,course)
t1.teaching()
