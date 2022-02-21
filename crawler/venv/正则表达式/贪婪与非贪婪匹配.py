import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$', content)
print(result)
print(result.group(1))      # 只匹配到7

# 因为.*会尽可能多的匹配字符，后面是\d+，也就是至少一个数字
# .*就把132456给匹配了，给\d+一个数字

# 解决方法：
# 变成.*?变成尽可能少的匹配字符，遇到可以与后面的\d+匹配的字符就停止
result = re.match('^He.*?(\d+).*Demo$', content)
print(result.group(1))  # 匹配到1234567

# plus: .不能匹配换行符，需要在match()的参数中加re.S
# plus: 如果目标字符串包含. ，可以用转义匹配：\.