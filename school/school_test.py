# import os
# import json
# def subject_modify():
#     student_name = input("学生姓名").strip()
#     try:
#         username = open("%s\\user_database\%s.json" % (os.getcwd(), student_name), 'r',encoding='utf-8')
#     except FileNotFoundError:
#         print('查无此人')
#     else:
#         username = json.load(username)
#         print(username)
#         if username['profession'] == 'teacher':
#             print('这个人是老师')
#             return subject_modify()
#         print('这是他%s的成绩：%s'%(username['subject'],username['subject']['go']))
#         teacher_modify= input('修改请按Y，不修改请按N')
#
#         if teacher_modify == "y" or teacher_modify == "Y":
#             while True:
#                 try:
#                     username_subject_number=int(input('输入要修改的数字'))
#                 except ValueError:
#                     print('写数字')
#                 else:
#                     username['subject']['go'] = username_subject_number
#                     print(username)
#                     continue
#         else:
#             return subject_modify()
# subject_modify()

class Person(object):
    def __init__(self,name,age,strength):
        self.name = name
        self.age = age
        self.strength = strength

    def talk(self):
        print('person is talking....')

class white_person(Person):
    pass


class Blac_Person(Person):

    def __init__(self,name,age,strength):#先继承，再重构
        Person.__init__(self,name,age,strength)
        print(self.name, self.age, self.strength)
        self.strength = 'high'
        print(self.name,self.age,self.strength)

    def talk(self):
        Person.talk(self)
        print('this is Blac_person talk')

    def walk(self):
        print('This is walk')

b = Blac_Person('aa',19,'low')