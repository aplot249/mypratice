#@author: sareeliu
#@date: 2021/5/13 20:18
import json,pathlib

class Student:
    # 姓名、年龄、电话
    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
    def __str__(self):
        return f'{self.name},{self.age},{self.tel}'

class ManageSystem:

    def __init__(self):
        self.student_list = []
        self.reload()
    @staticmethod
    def operate_output():
        output = '''
            1.增加学生
            2.删除学生
            3.改变学生
            4.查看所有学生
            5.保存学生
            6.退出程序
        '''
        print(output)
        operate_num = int(input("选择操作序号："))
        return operate_num
    def reload(self):
        if pathlib.Path("./student.txt").exists():
            with open("./student.txt") as f:
                self.student_list.extend([Student(student['name'],student['age'],student['tel']) for student in json.loads(f.read())])
    def run(self):
        while True:
            operate_num = self.operate_output()
            if operate_num == 1:
                self.add_student()
            if operate_num ==2:
                self.del_student()
            if operate_num == 3:
                self.update_student()
            if operate_num == 4:
                self.show_all_student()
            if operate_num == 5:
                self.save_student()
            if operate_num == 6:
                break
    def add_student(self):
        name,age,tel = [input("") for i in range(3)]
        student = Student(name,age,tel)
        self.student_list.append(student.__dict__)  # 插入属性字典
    def del_student(self):
        name = input("要删除的用户姓名:")
        for student in self.student_list:
            if student.name == str(name):
                self.student_list.remove(student)
    def update_student(self):
        name = input("更新那个学生信息:")
        student = [student for student in self.student_list if student.name == name][0]
        name,age,tel = [input("") for i in range(3)]
        student.name = name
        student.age = age
        student.tel = tel
    def show_all_student(self):
        if len(self.student_list) == 0:
            # 加载文件信息
            with open("./student.txt") as f:
                self.student_list.extend([Student(student['name'],student['age'],student['tel']) for student in json.loads(f.read())])
        for student in self.student_list:
            print(student)

    def save_student(self):
        with open('./student.txt','w') as f:
            f.write(json.dumps(self.student_list))
            f.flush()

manage = ManageSystem()
manage.run()