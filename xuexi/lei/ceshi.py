#@author: sareeliu
#@date: 2021/5/14 13:36
class Person:
    def __init__(self,name):
        self.name = name
        print("persion被调用了")
    def speak(self):
        print("人会说话")

class Mother(Person):
    def __init__(self,age,name):
        self.age = age
        Person.__init__(self,name)
        print("mother被调用了")
    def shenghaizi(self):
        print("mother会生孩子")

class Father(Person):
    def __init__(self,jjchang,name):
        self.jjchang = jjchang
        Person.__init__(self,name)
        print("father被调用了")
    def shejing(self):
        print("会射精")

class Haizi(Mother,Father):
    def __init__(self,yachi,name,age,jjchang):
        self.yachi = yachi
        Father.__init__(self,jjchang,name)
        Mother.__init__(self,age,name)
        print("haizi被调用了")
    def say(self):
        print("嘤嘤嘤")

print(Haizi.__mro__)
hz = Haizi(3,'liusri',10,28)
