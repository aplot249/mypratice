#@author: sareeliu
#@date: 2021/5/13 14:07

class Fu1:
    def __init__(self):
        self.word = "日父1"
    def say(self):
        print("fu1说"+self.word)

class Fu2:
    def __init__(self):
        self.word = "日父2"
    def say(self):
        print("fu2说"+self.word)

class Zi(Fu1,Fu2):
    def __init__(self):
        self.word = "日自己"
        self.__mao = "zijij"
    def saymao(self):
        print(self.__mao)
    def say(self):
        self.__init__()
        print("zi自己说"+self.word)
    def fu1_say(self):
        Fu1.__init__(self)
        Fu1.say(self)
    def fu2_say(self):
        Fu2.__init__(self)
        Fu2.say(self)
    def supersay(self):
        super(Zi, self).__init__()
        super(Zi, self).say()

zi = Zi()
# print(Zi.__mro__)
zi.say()
zi.fu1_say()
zi.fu2_say()
zi.say()
print("*"*20)
zi.supersay()
print(zi._Zi__mao)
zi.saymao()