def make_pizza(size, *toppings):              # *让python创建一个名为toppings的空元组
    """打印顾客点的所有配料"""
    print("\nMaking a" + str(size) + "pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

