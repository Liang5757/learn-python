import re

content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
pattern = re.compile('\d{2}:\d{2}')     # 正则字符串编译成正则表达式
tp = '\d{2}:\d{2}'
result1 = re.sub(tp, '', content1)
result2 = re.sub(pattern, '', content2)
print(result1)
print(result2)