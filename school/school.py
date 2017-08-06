# -*- coding: utf-8 -*-
class SchoolMember(object): #主校北京
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course
    def teaching(self):
        if self.course == 'c++':
            School_bj.tell(self)
    # def enroll(self):
    #     '''注册'''
    #     print('new school number [%s]'% self.name)
    #     SchoolMember.number += 1

    # def tell(self):
    #     print('-----info---:%s' % self.name)
    #     for k,v in self.__dict__.items():
    #         print('\t',k,v)

class School_bj(SchoolMember):

    def __init__(self,add):
        super(School_bj,self).__init__(name,age,course)
        self.add = add

    def tell(self):
        print('%s 老师在北京任课，教%s'%(self.name,self.course))

    #
    # def open_branch(self,addr):
    #     print('开分校在[%s]'%addr)

# class Teacher(SchoolMember):
#     def __init__(self,name,age,salary,course,school_obj):
#         # SchoolMember.__init__(self,name,age,sex)
#         super(Teacher,self).__init__(name,age,sex)
#         self.school = school_obj
#         self.salary = salary
#         self.course = course
#         self.enroll()#直接调用
#
#     def teaching(self):
#         print('Teacher [%s] is teaching [%s]'%(self.name,self.course))

# class Studenet(SchoolMember):
#     def __init__(self,name,age,course,tuition):
#         SchoolMember.__init__(self,name,age,sex)
#         self.course = course
#         self.tuition = tuition
#         self.enroll()
#         self.amount = 0
#
#     def pay_tuiton(self,amount):
#         print('student [%s] has just paied [%s]'%(self.name,amount))
#         self.amount += amount'c++'

name = 'a'
age = '18'
course =

t1 = SchoolMember(name,age,course)
t1.teaching()

#
# t1 = Teacher('a',18,'F**M',3000,'python','SH')
# s1 = Studenet('b',19,'N/A','PYS16',30000)
# s2 = Studenet('c',22,'M','PYS15',11000)
#
#
# s1.pay_tuiton(1)