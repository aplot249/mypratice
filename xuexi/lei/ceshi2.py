class Person:
    def __init__(self,name):
        self.name = name
        print("persion被调用了")
class Mother(Person):
    def __init__(self,name,age,jjchang):
        self.age = age
        super().__init__(name,jjchang)
        # super(Mother, self).__init__(name,jjchang)
        print("mother被调用了")
class Father(Person):
    def __init__(self,name,jjchang):
        self.jjchang = jjchang
        super().__init__(name)
        print("father被调用了")
    def pp(self):
        print("放屁")
class Haizi(Mother,Father):
    def __init__(self,yachi,name,age,jjchang):
        self.yachi = yachi
        super().__init__(name,age,jjchang)
        print("haizi被调用了")

print(Haizi.__mro__)
Haizi(3,'liusri',10,28)
