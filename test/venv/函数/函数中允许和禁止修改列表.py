def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#允许函数修改列表
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#禁止函数修改链表
print_models(unprinted_designs[:], completed_models)
#[:]会创建列表的副本使得函数无法改变列表