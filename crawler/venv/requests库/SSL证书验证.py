# 12306的证书没有被官方CA机构信任，所以以它做例子

import requests
from requests.packages import urllib3
import logging

# verify参数默认为True,会自动验证，可以把其设置为False

# 但这样会警告：提醒我们给它指定证书
# 可以设置忽略警告来屏蔽
urllib3.disable_warnings()
# 或者通过捕获警告到日志的方式忽略警告
logging.captureWarnings(True)
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

# 还可以指定一个本地证书用作客户端证书
# response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
