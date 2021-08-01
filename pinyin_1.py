#@author: sareeliu
#@date: 2021/4/5 17:08
from pypinyin import pinyin, lazy_pinyin, Style

print(lazy_pinyin('中心') )
print(lazy_pinyin('嗯'))
print(pinyin('中心', style=Style.FIRST_LETTER))
print(type(pinyin('中心', style=Style.FIRST_LETTER)))
