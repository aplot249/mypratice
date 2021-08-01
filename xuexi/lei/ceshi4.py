#@author: sareeliu
#@date: 2021/6/4 20:45

class A1:
    def speak(self):
        print('A1')
        super(A1, self).speak()


class A2:
    def speak(self):
        print('A2')
        super(A2, self).speak()


class B1:
    def speak(self):
        print('B1')
        super(B1, self).speak('文字')


class B2:
    # def __init__(self,name):
    #     self.name = name
    def speak(self,word):
        print('B2'+str(word))
        # print(self.name)

class AA(A1,A2):
    def speak(self):
        print('AA')
        super(AA, self).speak()


class BB(B1,B2):
    def speak(self):
        print('BB')
        super(BB, self).speak()


class C(AA,BB):
    def speak(self):
        print('C')
        super(C, self).speak()



print(C.__mro__)
c = C()
c.speak()