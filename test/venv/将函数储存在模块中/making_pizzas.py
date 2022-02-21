import pizza        # 导入pizza模块

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 还可以导入特定模块的特定函数
# from module_name import function_name
# 可以通过逗号分隔函数名
# from module_name import function_0, function_1, function_2
# 例如：from pizza import make_pizza
# 然后函数调用的时候只需要打函数名make_pizza

# 用as给函数取别名
# from pizza import make_pizza as mp
# 调用时只需要打别名mp

# 用as给模块指定别名
# import pizza as p
# 调用时打p.maka_pizza

# 用*号让模块pizza中的每一个函数都复制到这个程序文件中
# from pizza import *
# 使用时无需句点表示法
# 有可能导致函数名与自己使用的名称冲突