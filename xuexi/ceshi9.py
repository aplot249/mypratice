#@author: sareeliu
#@date: 2021/5/14 11:07
import copy
a = [1,2]
b = [3,4]
c = [a,b]
print("c地址为"+str(id(c)))
d = copy.copy(c)
print("d地址为"+str(id(d)))
e = copy.deepcopy(c)
print("e地址为"+str(id(e)))
print(id(c[0]))     # a元素地址167961928
print(id(d[0]))     # a元素地址167961928
print(id(e[0]))     # a元素地址167962248

ll = [1,2,3,4]
def myll(ll):
    ll.extend([5,6])
myll(ll)
# myll(copy.copy(ll))
print(ll)
print("&"*40)
def mydeepcopy(ll):
    ll.extend([5, 6])
    print(ll)
mydeepcopy(copy.deepcopy(ll))

print("*"*30)
g = a
print(id(a) == id(g))
h = copy.copy(a)
print(id(a) == id(h))
