#@author: sareeliu
#@date: 2021/5/13 17:53
__all__ = [
    'InputTooShort',
    # 'Myinput'
]

class InputTooShort(Exception):
    def __init__(self,str_len,min_len):
        self.str_len = str_len
        self.min_len = min_len
    def __str__(self):
        return "error! your input length is shorter than the min required length!"

class Myinput:
    def __init__(self,input_str):
        self.input_str = input_str
        self.min_len = 5
    @classmethod
    def read_input(cls):
        input_str = input("请输入：")
        return cls(input_str)
    def check_input(self):
        try:
            if len(self.input_str) < self.min_len:
                raise InputTooShort(len(self.input_str),self.min_len)
        except InputTooShort as res:
            print(res)
        else:
            print("输入正常！")

if __name__ == "__main__":
    myinput = Myinput.read_input()
    myinput.check_input()