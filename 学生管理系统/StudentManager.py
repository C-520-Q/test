from 学生管理系统.Student import Student


class StudentManager(object):
    def __init__(self):
        self.__students = []

    def add_student(self):
        name = input('请输入学生姓名：')
        age = int(input('请输入学生年龄：'))
        self.__students.append(Student(name, age))
        print('添加成功！')

    def view_list(self):
        for student in self.__students:
            print(student)

    def del_student(self):
        name = input('请输入要删除的学生姓名：')
        for student in self.__students:
            if student.name == name:
                self.__students.remove(student)
                print('删除成功！')
                break
        else:
            print('没有找到该学生！')

    def edit_student(self):
        name = input('请输入要修改的学生姓名：')
        for student in self.__students:
            if student.name == name:
                student.name = input('请输入新的学生姓名：')
                student.age = int(input('请输入新的学生年龄：'))
                print('修改成功！')
                break
        else:
            print('没有找到该学生！')

    def view_student(self):
        name = input('请输入要查询的学生姓名：')
        for student in self.__students:
            if student.name == name:
                print(student)
                break
        else:
            print('没有找到该学生！')

    def save_student(self):
        f = open('student.txt', 'w', encoding='utf-8')
            students = [s  for student in self.__students]
        f.write(str(students))
        f.close()

    def load_student(self):
        f = open('student.txt', 'r', encoding='utf-8')
        content = f.read()
        if not content:
            return
        self.__students = [Student(student['name'], student['age']) for student in eval(content)]
        f.close()

    @staticmethod
    def menu():
        print('-' * 40)
        print('欢迎使用传智教育学生管理系统V2.0')
        print('【1】添加学生信息')
        print('【2】删除学生信息')
        print('【3】修改学生信息')
        print('【4】查询学生信息')
        print('【5】遍历所有学生信息')
        print('【6】保存信息')
        print('【7】退出系统')
        print('-' * 40)

    def start(self):
        self.load_student()
        while True:
            StudentManager.menu()
            user_input = int(input('请输入选项：'))
            if user_input == 1:
                self.add_student()
            elif user_input == 2:
                self.del_student()
            elif user_input == 3:
                self.edit_student()
            elif user_input == 4:
                self.view_student()
            elif user_input == 5:
                self.view_list()
            elif user_input == 6:
                self.save_student()
            elif user_input == 7:
                print('欢迎下次使用！')
                break
            else:
                print('输入有误，请重新输入！')
