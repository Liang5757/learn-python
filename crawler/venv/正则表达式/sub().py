import re

content = '65ab65bc64ds6464dasd'
# 第一个参数为匹配格式，第二个参数为替换字符串，第三个为原字符串
content = re.sub('\d+', '', content)        # 删除所有数子
print(content)