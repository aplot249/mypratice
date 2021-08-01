#@author: sareeliu
#@date: 2021/5/13 14:07

class Fu1:
    def __init__(self):
        self.word = "日父1"
    def say(self):
        print("fu1说"+self.word)

class Fu2(Fu1):
    def __init__(self):
        self.word = "日父2"
    def say(self):
        print("fu2说"+self.word)
        super().__init__()
        super().say()

class Zi(Fu2):
    def __init__(self):
        self.word = "日自己"
    def say(self):
        self.__init__()
        print("zi自己说"+self.word)
    def fu1_say(self):
        Fu1.__init__(self)
        Fu1.say(self)
    def fu2_say(self):
        Fu2.__init__(self)
        Fu2.say(self)
    def old_say(self):
        Fu1.__init__(self)
        Fu1.say(self)
        Fu2.__init__(self)
        Fu2.say(self)
    def new_say(self):
        # super(Zi, self).say()
        super().__init__()
        super().say()
zi = Zi()
# print(Zi.__mro__)
zi.say()
zi.fu1_say()
zi.fu2_say()
zi.say()
print("*"*20)
zi.old_say()
print("*"*20)

zi.new_say()