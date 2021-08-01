#@author: sareeliu
#@date: 2021/6/4 20:57
class A:
    def __init__(self,name):
        self.name = name
    def say(self):
        print(self.name)

class B(A):
    def say(self):
        print('B')
        print(self,self.name)
        super(B, self).say()

class C(B):
    def say(self):
        print('C')
        super(C, self).say()

c = C('saree')
print(C.__mro__)
c.say()