#@author: sareeliu
#@date: 2021/5/14 12:27
# import mycommon
from mycommon import input_final

def theinput():
    input_str = input("输入：")
    print("正在进行输入工作")
    global input_final
    input_final = True
    # mycommon.input_final = True

def check_input():
    # if mycommon.input_final:
    if input_final:
        print("输入工作已完成")
    else:
        print("输入工作还未完成")