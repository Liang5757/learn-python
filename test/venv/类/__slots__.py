class Student(object):
    pass

s = Student()
s2 = Student()
s.name = 'zhengliang'       # 给实例绑定属性
print(s.name)

def set_age(self, age):
    self.age = age

def set_score(self, score):
    self.score = score

from types import MethodType

s.set_age = MethodType(set_age, s)      # 给实例绑定方法(对其他实例不可见)
s.set_age(25)   # 调用实例方法
print(s.age)

Student.set_score = set_score       # 给类绑定方法，对所有实例可见
s.set_score(100)
print(s.score)
s2.set_score(90)
print(s2.score)

# 使用__slots__限制实例的属性
class Student_2(object):
    __slots__ = ('name', 'age')     # 用tuple定义允许绑定的属性名称
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
