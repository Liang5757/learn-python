favorite_languages = {                          #字典中储存列表
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edword': ['ruby', 'go'],
    'phil': ['python', 'haskell'],              #结尾留逗号为下一次增加键-值对做准备
}

for name, languages in favorite_languages.items():          #items()返回一个键值对列表
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())




