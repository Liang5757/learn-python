# 类的创建
class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):      #__init__()没当根据Dog类创建新实例时，python会自动运行它
        """初始化属性name和age"""
        self.name = name        #self为前缀的变量都可供类的所有方法使用
        self.age = age

    def sit(self):      # 每个与类相关联的方法都自动传递实参self,是一个指向实例本身的引用，让实例可以访问类中的属性和方法
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

# 根据类创建实例
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)           可以创建多个实例

print("My dog's name is " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + " years old.")

# 调用方法
my_dog.sit()
my_dog.roll_over()