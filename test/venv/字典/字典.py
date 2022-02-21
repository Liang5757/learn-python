favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edword': 'ruby',
    'phil': 'python',              #结尾留逗号为下一次增加键-值对做准备
}

#添加键-值对
favorite_languages['zhengliang'] = 'python'

#修改键-值对
favorite_languages['sarah'] = 'python'

#删除键-值对
del favorite_languages['sarah']

for name in favorite_languages.keys():              #key()返回键
    print(name)

print("************万恶的分割符************")

for languages in set(favorite_languages.values()):       #value()返回值
    print(languages)                                     #set()提取所有不同的元素构成字典
