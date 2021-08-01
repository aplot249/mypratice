#@author: sareeliu
#@date: 2021/5/13 16:24
# 实现多态，对一个基类，针对同一个方法名，有不同的实现，调用这同一个方法名，做到不同的实现。

class Dog:
    def walk(self):
        pass
    
class ArmyDog(Dog):
    def walk(self):
        print("抓小偷")
        
class DrugDog(Dog):
    def walk(self):
        print("抓毒品")
        
class Person:
    def walk_with_dog(self,dog):
        dog.walk()

ad = ArmyDog()
dd = DrugDog()
pp = Person()
pp.walk_with_dog(dd)
pp.walk_with_dog(ad)