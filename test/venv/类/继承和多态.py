class Animal(object):
    def run(self):
        print("animal is running")

class Dog(Animal):      # 继承：Animal是Dog的父类，Dog从父类获得所有功能
    pass

class Cat(Animal):
    def run(self):          # 多态：子类的run()覆盖父类的run() 、
        print('Cat is running')

my_dog = Dog()
my_dog.run()

my_cat = Cat()
my_cat.run()

print(isinstance(my_dog, Animal))       # 子类与父类的类型相同
#当一个函数的参数为父类时，可以传入子类的实例，而不用任何修改

# 开闭原则：1：对扩展开放（允许新增Animal类） 2：对修改封闭（不需要修改依赖Animal类型的函数）

# 鸭子类型：传参时不一定要传Animal类型，只要保证传入对象有一个run()方法就行
# 只要看起来像鸭子，走起来像鸭子，就可以被看作是鸭子
