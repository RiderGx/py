# -*- coding: utf-8 -*-
import json
class SchoolMember(object): #学校模板
    def __init__(self,name,course):
        self.name = name
        self.course = course

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
        super(School_bj,self).__init__(name,course)
        self.class_list = []

    def School_list(self):
        School_sh_list = input('选择查看')
        if School_sh_list == 'a':
            return School_sh.creat_class(self)

    # def tell(self):
    #     print('%s 老师在上海任课，教%s'%(self.name,self.course))

    def class_list_add(self):
        self.class_list.append(self.name)

    def creat_class(self):
        with open('class_number','r',encoding='utf-8') as class_list_number:
            class_list_number = class_list_number.read()
            class_name =  self.name + '\t'+'go' + '\t'+class_list_number
            class_personnel = {'teacher':self.name,'student':[]}
            with open('%s.json'%(class_name) , 'w', encoding='utf-8') as class_name_file:
                json.dump(class_personnel,class_name_file)
            class_list_number = int(class_list_number)
            class_list_number += 1
            class_list_number = str(class_list_number)
            with open('class_number', 'w', encoding='utf-8') as new_class_list_number:
                new_class_list_number.write(class_list_number)





name = 'a'
course = input('输入教学学科').strip()



t1 = SchoolMember(name,course)
t1.teaching()
