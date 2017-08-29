# -*- coding: utf-8 -*-
import pickle
import os

class User_data(object):
    def __init__(self,name):
        self.name = name

    def User_Authentication(self):
        '''用户认证'''
        if self.name == 'root':
            password = input('输入管理员密码：').strip()
            if password == 'root':
                print('创建班级选1，新增老师选2')
                while True:
                        root_input = input('1 or 2:').strip()
                        if root_input == '1':
                            print('创建完后按r，可继续创建')
                            return User_data.root_creat_class(self)
                        elif root_input == '2':
                            return User_data.Teacher_registration(self)
                        else:
                            continue
        else:
            try:
                username =  open(r"%s\user_database\%s"%(os.getcwd(),self.name), 'rb')
            except FileNotFoundError:
                return User_data.Student_registration(self)
            else:
                user_data = pickle.load(username)
                password = input('输入密码>>>>>:').strip()
                if self.name == user_data['name'] and password == user_data['password']:
                    SchoolMember(user_data)
                else:
                    print('账号密码错误')

    def root_creat_class(self):
        while True:
            add = ''
            subject = input('输入学科,输入q退出程序:').strip()
            if subject == 'python' or subject == 'linux':
                add = 'BJ'
            elif subject == 'go':
                add = 'SH'
            elif subject == 'q':
                exit()
            else:
                continue
            self.subject = subject
            self.profession = 'root'
            return SchoolMember.creat_class(self, add)

    def Teacher_registration(self):
        '''初始老师'''
        while True:
            teacher_name = input('输入教师姓名>>>>>>:').strip()
            if teacher_name == 'root' or  teacher_name == 'admin':continue
            pasth = r"%s\user_database\%s"%(os.getcwd(),teacher_name)
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
        return User_data.User_Authentication(self)

    def creat_class(self,add):
        '''创建班级'''
        n = 0
        path = r'%s\%s\class\%s' % (os.getcwd(),add,self.subject)
        for root, a, f in os.walk(path):
            for i in f:
                n += 1
        n = str(n+1)
        class_name =  self.subject + '-' + n + '班'
        class_personnel = {'teacher': '','student':[]}
        with open(r"%s\%s"%(path,class_name) , 'wb') as class_name_file:
            pickle.dump(class_personnel,class_name_file)
            class_name_file.flush()
            return SchoolMember.class_list_add(self,add,self.subject)

    def class_list_add(self,add,subject):
        '''查看和加入班级'''
        path = r"%s\%s\class\%s" %(os.getcwd(),add,subject)
        list = []
        for root, dirs, files in os.walk(path):
            for i in files:
                list.append(i)
        for index, item in enumerate(list,1):
            print(index, item)
        while True:
            user_choice = input("选择班级加入>>>:")
            if user_choice == 'r' and self.name == 'root':return User_data.root_creat_class(self)
            elif user_choice == 'q' and self.name == 'root':exit()
            else:
                if self.profession == 'root':
                    print('无法加入')
                    return User_data.root_creat_class(self)
                if self.profession == 'student':
                    self.subject[subject] = 0
                user_choice = int(user_choice)- 1
            try:
                class_list = list[user_choice]
            except IndexError:
                print('输入错误')
            else:
                with open(r"%s\%s"%(path,class_list),'rb')as class_list_f_r:
                    class_list_name = pickle.load(class_list_f_r)
                    if self.profession == 'teacher':
                        class_list_name['teacher'] = self.user_data['name']
                    elif self.profession ==  'student':
                        class_list_name['student'].append(self.name)
                    print(class_list_name)
                    with open(r"%s\%s" % (path, class_list), 'wb')as class_list_f_w:
                         pickle.dump(class_list_name,class_list_f_w)
                    if subject == 'go':
                        return School_sh.Hello_user(self)
                    else:
                        return School_bj.Hello_user(self)

    def data_inquiry(self,add):
        '''数据查询，查姓名'''
        subject = ''
        inquiry = input('输入想查询的职务，1是老师，2是学生>>>>>：')
        if inquiry == '1':
            inquiry = 'teacher'
        elif inquiry == '2':
            inquiry = 'student'
        else:
            print('输入错误')
            return SchoolMember.data_inquiry(self, add)
        data_name = input('输入想查询的姓名>>>>>：')
        if self.profession == 'teacher':
            subject = self.subject
            FindPath = r'%s\%s\class\%s' % (os.getcwd(), add, subject)
            FileNames = os.listdir(FindPath)
        else:
            subject = self.subject.keys()
            for i in subject:
                FindPath = r'%s\%s\class\%s' % (os.getcwd(), add, i)
                FileNames = os.listdir(FindPath)
        for file_name in FileNames:
            fullfilename = os.path.join(FindPath, file_name)
            with open(fullfilename, 'rb') as file_name_r:
                class_data = pickle.load(file_name_r)
                for i in class_data:
                    if i == inquiry and data_name in class_data[i]:
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
            username = open(r"%s\user_database\%s" % (os.getcwd(), student_name), 'rb')
        except FileNotFoundError:
            print('查无此人')
            return SchoolMember.teacher_life(self)
        else:
            username = pickle.load(username)
            if username['profession'] == 'teacher':
                print('这个人是老师')
                return SchoolMember.teacher_life(self)
            if self.subject in username['subject']:
                subject = username['subject'][self.subject]
                print('这是%s的成绩：%s' % (student_name,subject))
                teacher_modify = input('修改请按Y，不修改请按N')
                if teacher_modify == "y" or teacher_modify == "Y":
                    while True:
                        try:
                            username_subject_number = int(input('输入要修改的数字'))
                        except ValueError:
                            print('写数字')
                            return SchoolMember.teacher_life(self)
                        else:
                            username['subject'][self.subject] = username_subject_number
                            with open(r"%s\user_database\%s" % (os.getcwd(),student_name), 'wb') as student_w:
                                pickle.dump(username,student_w)
                            return SchoolMember.teacher_life(self)
                else:
                    return SchoolMember.teacher_life(self)
            else:
                print('这个学生没有你的学科')
                return SchoolMember.teacher_life(self)


    def teacher_class(self):
        teacher_name = self.name
        subject = self.subject
        add = self.location
        FindPath = r'%s\%s\class\%s' % (os.getcwd(), add, subject)
        FileNames = os.listdir(FindPath)
        for file_name in FileNames:
            fullfilename = os.path.join(FindPath, file_name)
            with open(fullfilename, 'rb') as file_name_r:
                class_data = pickle.load(file_name_r)
                if teacher_name == class_data['teacher']:
                    fullfilename = fullfilename.split('\\')[-1]
                    fullfile = fullfilename.split('.')[0]
                    print('班级：%s\t学生：%s'%(fullfile,class_data['student']))
        if self.profession == 'student':
             return SchoolMember.student_life(self)
        elif self.profession == 'teacher':
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
        '''上海分校的校园列表'''
        if self.profession == 'teacher':
            return School_sh.creat_class(self,'SH')
        elif self.profession == 'student':
            return School_sh.class_list_add(self,'SH','go')

    def Hello_user(self):
        '''hey，用户，当老师注册完毕后，结束，而学生则直接进入校园生活'''
        self.user_data['location'] = 'SH'
        self.user_data['subject'] = self.subject
        with open(r"%s\user_database\%s" % (os.getcwd(), self.name,), 'wb') as student_w:
             pickle.dump(self.user_data, student_w)
             student_w.flush()
        if self.profession == 'teacher':
            if self.name == 'root':
                print('完成老师注册，请用老师账号登录')
                exit()
            else:
                return School_sh.teacher_life(self)
        else:
            return School_sh.student_life(self)

    def student_life(self):
        '''上海学生的校园生活'''
        while True:
            print('欢迎回来[%s]，你可以做以下操作' % self.name)
            print('a是查询你的基本资料，b只查询的成绩，c查询除你以外用户所在班级,'
                  '输入q程序结束')
            student_chroice = input('请根据提示输入指令')
            if student_chroice == 'a':
                print('姓名:{0}\t'
                      '职业:{1}\t'
                      '学科:{2}\t'
                      '所在学校:{3}'.format(self.name, self.profession, self.subject, '上海分校'))
                return School_sh.student_life(self)
            elif student_chroice == 'b':
                print(self.subject)
                return School_sh.student_life(self)
            elif student_chroice == 'c':
                return SchoolMember.data_inquiry(self,'SH')
            elif student_chroice == 'q':
                exit()
            else:
                continue

    def teacher_life(self):
        '''重新登录后的上海老师生活'''
        print('欢迎回来[%s]老师，你可以做以下操作' %self.name)
        print('a是查询你的基本资料，b修改学生的成绩，c查询除你以外用户所在班级，e查询你上课的班级,'
              'f加入一个新的班级，q退出程序')
        while True:
            teacher_chroice = input('请根据提示输入指令')
            if teacher_chroice == 'a':
                print('姓名:{0}\t'
                      '职业:{1}\t'
                      '学科:{2}\t'
                      '所在学校:{3}'.format(self.name, self.profession, self.subject, '上海分校'))
                return School_sh.teacher_life(self)
            elif teacher_chroice == 'b':
                return School_sh.subject_modify(self)
            elif teacher_chroice == 'c':
                return SchoolMember.data_inquiry(self, 'SH')
            elif teacher_chroice == 'e':
                return SchoolMember.teacher_class(self)
            elif teacher_chroice == 'f':
                return SchoolMember.class_list_add(self,'SH',self.subject)
            elif teacher_chroice == 'q':
                exit()
            else:
                continue


class School_bj(SchoolMember):
    '''定义了北京的分校'''
    def __init__(self,user_data):
        super(School_bj,self).__init__(name,user_data)

    def School_list(self,user_chroice):
        self.user_data['subject'] = user_chroice
        if self.profession == 'teacher':
             return School_bj.creat_class(self,'BJ')
        elif self.profession == 'student':
             return School_bj.class_list_add(self,'BJ',user_chroice)

    def Hello_user(self):
        self.user_data['location'] = 'BJ'
        self.user_data['subject'] = self.subject
        with open(r"%s\user_database\%s" % (os.getcwd(), self.name,), 'wb') as student_w:
            pickle.dump(self.user_data, student_w)
            student_w.flush()
        if self.profession == 'teacher':
            if self.name == 'root':
                print('完成老师注册，请用老师账号登录')
                exit()
            else:
                return School_sh.teacher_life(self)
        else:
            return SchoolMember.student_life(self)

    def student_life(self):
        while True:
            print('欢迎回来[%s]学生，你可以做以下操作' % self.name)
            print('a是查询你的基本资料，b只查询的成绩，c查询除你以外用户所在班级，e选择其他学科,'
                  '输入q程序结束')
            student_chroice = input('请根据提示输入指令')
            if student_chroice == 'a':
                print('姓名:{0}\t'
                      '职业:{1}\t'
                      '学科:{2}\t'
                      '所在学校:{3}'.format(self.name, self.profession, self.subject, '北京分校'))
                return School_bj.student_life(self)
            elif student_chroice == 'b':
                print(self.subject)
                return School_bj.student_life(self)
            elif student_chroice == 'c':
                return SchoolMember.data_inquiry(self,'BJ')
            elif student_chroice == 'e':
                return School_bj.student_other_subject(self)
            elif student_chroice == 'q':
                print('程序结束')
                exit()
            else:
                continue

    def student_other_subject(self):
        while True:
            user_new_subject = input('输入想学的新学科').strip()
            if user_new_subject == 'linux' or user_new_subject == 'python':
                if user_new_subject in self.subject:
                    print('科目已经存在')
                else:
                    self.subject[user_new_subject] = 0
                    with open(r"%s\user_database\%s" % (os.getcwd(), self.name,), 'wb',
                              ) as student_w:
                        pickle.dump(self.user_data, student_w)
                        student_w.flush()
                        break
            elif user_new_subject == 'go':
                print('此不属于我们学校的办理课程')
            else:
                print('输入错误')
                continue
        return SchoolMember.class_list_add(self, 'BJ', user_new_subject)



    def teacher_life(self):
        print('欢迎回来[%s]老师，你可以做以下操作' %self.name)
        print('a是查询你的基本资料，b修改学生的成绩，c查询除你以外用户所在班级，e查询你上课的班级,'
              'f加入一个新的班级，q退出程序')
        while True:
            teacher_chroice = input('请根据提示输入指令')
            if teacher_chroice == 'a':
                if teacher_chroice == 'a':
                    print('姓名:{0}\t'
                          '职业:{1}\t'
                          '学科:{2}\t'
                          '所在学校:{3}'.format(self.name, self.profession, self.subject,'北京分校'))
                return School_bj.teacher_life(self)
            elif teacher_chroice == 'b':
                return School_bj.subject_modify(self)
            elif teacher_chroice == 'c':
                return SchoolMember.data_inquiry(self, 'BJ')
            elif teacher_chroice == 'e':
                return SchoolMember.teacher_class(self)
            elif teacher_chroice == 'f':
                return SchoolMember.class_list_add(self,'BJ',self.subject)
            elif teacher_chroice == 'q':
                exit()
            else:
                continue


name = input('请输入你的大名>>>>>>:').strip()
a = User_data(name)
a.User_Authentication()