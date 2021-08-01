#@author: sareeliu
#@date: 2021/5/13 17:12
try:
    # hh = 'ddsd'
    try:
        print(hh)
    except NameError as res:
        print("nameerror错误")
        print(res)
    else:
        print("没有出错")
    finally:
        print("终究执行！")
except Exception:
    print("出错！！！")