# -*- coding: utf-8 -*-
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
                # print('判断生效')
                user_data = json.load(username)
                SchoolMember(user_data)

    def Teacher_registration(self):
        '''初始老师'''
        teacher_name = input('输入教师姓名>>>>>>:').strip()
        profession = 'teacher'
        subject = ''
        user_data = {'name': teacher_name, 'profession': profession, 'subject': subject,'location':''}
        SchoolMember(user_data)

    def Student_registration(self):
        '''初始学生'''
        profession = 'student'
        subject = {}
        user_data= {'name':self.name,'profession':profession,'subject':subject,'location':''}
        SchoolMember(user_data)


class SchoolMember(object): #学校模板
    def __init__(self,user_data):
        self.name = user_data['name']
        self.profession = user_data['profession']
        self.subject = user_data['subject']
        self.location = user_data['location']
        self.user_data = user_data
        if len(self.subject) == 0:
            SchoolMember.user_chorice(self)
        elif self.profession == 'student':
            SchoolMember.student_life(self)
        elif self.profession == 'teacher':
            SchoolMember.teacher_life(self)

    def user_chorice(self):
        '''选择学科，通过学科选择学校'''
        while True:
            user_chorice_data = input('请输入学科>>>>>:').strip()
            if self.profession == 'teacher':
                self.subject = user_chorice_data
            if user_chorice_data == 'linux' or user_chorice_data == 'python':
                School_bj.School_list(self,user_chorice_data)
            elif user_chorice_data == 'go':
                School_sh.School_list(self)
            else:
                print('学科输入错误')

    def creat_class(self,add):
        n = 0
        path = '%s\%s\class\%s' % (os.getcwd(),add,self.subject)
        for root, a, f in os.walk(path):
            for i in f:
                n += 1
        n = str(n+1)
        class_name =  self.subject + '-' + n + '班'
        class_personnel = {'teacher': '','student':[]}
        with open("%s\%s.json"%(path,class_name) , 'w', encoding='utf-8') as class_name_file:
            json.dump(class_personnel,class_name_file)
            class_name_file.flush()
            return SchoolMember.class_list_add(self,add,self.subject)

    def class_list_add(self,add,subject):
        '''查看和加入班级'''
        path = "%s\%s\class\%s" %(os.getcwd(),add,subject)
        list = []
        for root, dirs, files in os.walk(path):
            for i in files:
                list.append(i)
        for index, item in enumerate(list,1):
            print(index, item)
        while True:
            user_choice = input("选择班级加入>>>:")
            if user_choice == 'q':return  SchoolMember(self)
            else:
                if self.profession == 'student':
                    self.subject[subject] = 0
                user_choice = int(user_choice)- 1
            try:
                class_list = list[user_choice]
            except IndexError:
                print('输入错误')
            else:
                with open("%s\%s"%(path,class_list),'r',encoding='utf-8')as class_list_f_r:
                    class_list_name = json.load(class_list_f_r)
                    if self.profession == 'teacher':
                        class_list_name['teacher'] = self.user_data['name']
                    elif self.profession ==  'student':
                        class_list_name['student'].append(self.name)
                    print(class_list_name)
                    with open("%s\%s" % (path, class_list), 'w')as class_list_f_w:
                         json.dump(class_list_name,class_list_f_w)
                    if subject == 'go':
                        return School_sh.Hello_user(self)
                    else:
                        return School_bj.Hello_user(self)

    def data_inquiry(self,add):
        '''数据查询，查姓名'''
        # print(self.subject)
        FindPath = '%s\%s\class\%s' % (os.getcwd(),add,self.subject)
        FileNames = os.listdir(FindPath)
        inquiry = input('输入想查询的职务，1是老师，2是学生>>>>>：')
        if inquiry == '1':inquiry = 'teacher'
        elif inquiry == '2':inquiry = 'student'
        else:
            print('输入错误')
            return SchoolMember.data_inquiry(self,add)
        data_name = input('输入想查询的姓名>>>>>：')
        for file_name in FileNames:
            fullfilename = os.path.join(FindPath, file_name)
            with open(fullfilename, 'r') as file_name_r:
                class_data = json.load(file_name_r)
                list= []
                for i in class_data:
                        # print(i,":",class_data[i])
                    if i == inquiry and data_name in class_data[i]:
                        list.append(fullfilename)
                        fullfilename = fullfilename.split('\\')[-1]
                        fullfile = fullfilename.split('.')[0]
                        print(fullfile)
        if self.profession == 'student':
            return SchoolMember.student_life(self)
        elif self.profession == 'teacher':
            return SchoolMember.teacher_life(self)

    def subject_modify(self):
        student_name = input("姓名").strip()
        try:
            username = open("%s\\user_database\%s.json" % (os.getcwd(), student_name), 'r', encoding='utf-8')
        except FileNotFoundError:
            print('查无此人')
        else:
            username = json.load(username)
            print(username)
            if username['profession'] == 'teacher':
                print('这个人是老师')
                return SchoolMember(self)
            if self.subject in username['subject']:
                print('这是%s的成绩：%s' % (username['subject'], username['subject'][self.subject]))
                teacher_modify = input('修改请按Y，不修改请按N')

                if teacher_modify == "y" or teacher_modify == "Y":
                    while True:
                        try:
                            username_subject_number = int(input('输入要修改的数字'))
                        except ValueError:
                            print('写数字')
                        else:
                            username['subject'][self.subject] = username_subject_number
                            print(username)
                            return SchoolMember.teacher_life(self)
            else:
                print('这个学生没有你的学科')
                return SchoolMember.teacher_life(self)

    def student_life(self):
        '''学生生活'''
        if self.location == 'SH':
            return School_sh.student_life(self)
        else:
            return School_bj.student_life(self)

    def teacher_life(self):
        '''教师生活'''
        if self.location == 'SH':
            return School_sh.teacher_life(self)
        else:
            return School_bj.teacher_life(self)


class School_sh(SchoolMember):
    '''定义了上海的分校'''
    def __init__(self):
        super(School_sh,self).__init__(self)
        self.user_data['subject'] = 'go'

    def School_list(self):
        if self.profession == 'teacher':
            return School_sh.creat_class(self,'SH')
        elif self.profession == 'student':
            return School_sh.class_list_add(self,'SH','go')

    def Hello_user(self):
        self.user_data['location'] = 'SH'
        self.user_data['subject'] = 'go'
        # print(self.user_data)
        with open("%s\\user_database\%s.json" % (os.getcwd(), self.name,), 'w', encoding='utf-8') as student_w:
            json.dump(self.user_data, student_w)
        if self.profession == 'teacher':
            print('完成老师注册，请用老师账号登录')
            exit()
        else:
            return User_data.User_Authentication(self)

    def student_life(self):
        print('欢迎回来[%s]学生，你可以做以下操作' % self.name)
        print('a是查询你的基本资料，b只查询的成绩，c查询除你以外用户所在班级随便'
              '输入程序结束')
        student_chroice = input('请根据提示输入指令')
        if student_chroice == 'a':
            print('a')
            for key in self.user_data:
                print(key,":",self.user_data[key])
            return School_sh.student_life(self)
        elif student_chroice == 'b':
            print(self.subject)
            return School_sh.student_life(self)
        elif student_chroice == 'c':
            return SchoolMember.data_inquiry(self,'SH')
        else:
            exit()

    def teacher_life(self):
        print('欢迎回来[%s]老师，你可以做以下操作' %self.name)
        print('a是查询你的基本资料，b修改学生的成绩，c查询除你以外用户所在班级，随便'
              '输入程序结束')
        teacher_chroice = input('请根据提示输入指令')
        if teacher_chroice == 'a':
            print('a')
            for key in self.user_data:
                print(key, ":", self.user_data[key])
            return School_sh.teacher_life(self)
        elif teacher_chroice == 'b':
            return School_sh.subject_modify(self)
        elif teacher_chroice == 'c':
            return SchoolMember.data_inquiry(self, 'SH')
        else:
            exit()


class School_bj(SchoolMember):
    '''定义了北京的分校'''
    def __init__(self,user_data):
        super(School_bj,self).__init__(name,user_data)

    def School_list(self,user_chroice):
        self.user_data['subject'] = user_chroice
        if self.profession == 'teacher':
             return School_bj.creat_class(self,'bj')
        elif self.profession == 'student':
             return School_sh.class_list_add(self,'bj',user_chroice)

    def Hello_user(self):
        self.user_data['location'] = 'BJ'
        print(self.user_data)
        with open("%s\\user_database\%s.json" % (os.getcwd(), self.name,), 'w', encoding='utf-8') as student_w:
            json.dump(self.user_data, student_w)
        if self.profession == 'teacher':
            print('完成老师注册，请用老师账号登录')
            exit()
        else:
            return User_data.User_Authentication(self)

    def student_life(self):
        print('欢迎回来[%s]学生，你可以做以下操作' % self.name)
        print('a是查询你的基本资料，b只查询的成绩，c查询除你以外用户所在班级，随便'
              '输入程序结束')
        student_chroice = input('请根据提示输入指令')
        if student_chroice == 'a':
            print('a')
            for key in self.user_data:
                print(key,":",self.user_data[key])
            return School_sh.student_life(self)
        elif student_chroice == 'b':
            print(self.subject)
            return School_sh.student_life(self)
        elif student_chroice == 'c':
            return SchoolMember.data_inquiry(self,'BJ')
        else:
            print('输出错误，程序结束')
            exit()

    def teacher_life(self):
        print('欢迎回来[%s]老师，你可以做以下操作' %self.name)
        print('a是查询你的基本资料，b修改学生的成绩，c查询除你以外用户所在班级，随便'
              '输入程序结束')
        teacher_chroice = input('请根据提示输入指令')
        if teacher_chroice == 'a':
            print('a')
            for key in self.user_data:
                print(key, ":", self.user_data[key])
            return School_sh.teacher_life(self)
        elif teacher_chroice == 'b':
            return School_sh.subject_modify(self)
        elif teacher_chroice == 'c':
            return SchoolMember.data_inquiry(self, 'BJ')
        else:
            print('输出错误，程序结束')
            exit()



name = input('请输入你的大名>>>>>>:').strip()
a = User_data(name)
a.User_Authentication()