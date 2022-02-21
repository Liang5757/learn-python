import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get('http://maoyan.com/board/4', headers = headers)
song_name_result = re.findall('<a.*?title=.*?>(.*?)</a>', r.text, re.S)
# findall()获得所有匹配成功的所有内容
# 返回类型为列表，列表中的每一个元素都是元组
for song_name in song_name_result:
    print(song_name)