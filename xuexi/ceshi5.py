#@author: sareeliu
#@date: 2021/5/13 16:47
class Fu:
    __good = [1,2,3,4,5]
    @classmethod
    def show_goods(cls):
        print(cls.__good)

Fu.show_goods()
fu = Fu()
fu.show_goods()


class Zi(Fu):
    pass

print("*"*30)
zi = Zi()
zi.show_goods()