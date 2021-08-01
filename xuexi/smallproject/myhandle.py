#@author: sareeliu
#@date: 2021/5/14 12:30
# import mycommon
from mycommon import handle_final

def thehandle():
    print("正在进行处理工作")
    # mycommon.handle_final = True
    global handle_final
    handle_final = True

def check_handle():
    # if mycommon.handle_final:
    if handle_final:
        print("处理工作完成")
    else:
        print("处理工作还未完成")