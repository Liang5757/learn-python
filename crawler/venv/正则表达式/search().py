import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.match('Hello.*?(\d+).*?Demo', content)      # match()只要开头不匹配就失败，返回NULL
print(result)

result = re.search('Hello.*?(\d+).*?Demo', content)     # search()匹配扫描整个字符串
print(result)

