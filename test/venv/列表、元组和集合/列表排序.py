grade = [98, 99, 97, 100, 100, 96, 94, 95, 100, 85]
print("原列表：", grade)
grade.sort()                            #进行升序排序
print("升序：", grade)
grade.sort(reverse = True)              #进行降序排序
print("降序：", grade)

#listname.sort(key = None, reverse = False)
#key:表示指定从每个元素中提取一个用于比较的键（例如，设置“key = str.lower”表示排序时不区分字母大小写）
print("************万恶的分割符************")


password = [50, 43, 97, 60, 63, 95, 94, 95, 154, 85]
print("原列表：", password)
password_as = sorted(password)                              #进行升序排序
print("升序：", password_as)
password_as = sorted(password ,reverse = True)              #进行降序排序
print("降序：", password_as)

#sorted()会建立一个原列表的副本
print("************万恶的分割符************")

#列表逆置
password = [50, 43, 97, 60, 63, 95, 94, 95, 154, 85]
print(password)
password.reverse()          #reverse()函数会使列表逆置
print(password)
