import requests
from urllib.parse import urlencode

class Parse(object):
    def __init__(self):
        # 模拟chrome浏览器
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                           (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        self.headers = {'User-Agent': self.user_agent}

    # 获得搜素页面的源码
    def getPage(self, w):
        params = {
            'new_json': '1',
            'remoteplace': 'txt.yqq.song',
            't': '0',
            'aggr': '1',
            'cr': '1',
            'catZhida': '1',
            'lossless': '0',
            'flag_qc': '0',
            'p': '1',
            'n': '20',
            'w': w,
            'g_tk': '5381',
            'format': 'json',
            'inCharset': 'utf8',
            'outCharset': 'utf-8',
            'notice': '0',
            'platform': 'yqq.json',
            'needNewCode': '0',
        }

        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?' + urlencode(params)
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return response.json()
        except requests.ConnectionError:
            return None

    # 过滤得到歌曲信息
    def getSongInfo(self, json):
        singer_name = []
        if json.get('data').get('song').get('list'):
            for item in json.get('data').get('song').get('list'):
                song_name = item.get('title')
                song_mid = item.get('mid')
                song_time = item.get('interval')
                if item.get('singer'):
                    for singer in item.get('singer'):
                        singer_name.append(singer.get('name'))
                yield {
                    'song_name': song_name,
                    'singer_name': singer_name,
                    'song_mid': song_mid,
                    'song_time': song_time,
                }
                singer_name = []

    # 从爬取的所有歌曲中获得选择的歌曲的信息
    def selectSong(self, song_infos, num):
        for i, item in enumerate(song_infos):
            if i == num:
                return item
            elif i > num:
                print('输入错误！')
                break

    # 输出歌曲信息
    def printInfo(self, song_info):
        for num, item in enumerate(song_info):
            print(num,' 歌名:', item['song_name'], end='   ')
            print('歌手:', '/'.join(item['singer_name']), end='   ')
            minutes = item['song_time']//60
            seconds = item['song_time']-60*minutes
            print('时长:%02d:%02d' % (minutes, seconds))

    # # 获取歌曲时长
    # def getSongDuration(self, song_info):
    #     return song_info['song_time']

    # 获取歌曲的下载url
    def getSongUrl(self, song_info):
        song_mid = song_info['song_mid']
        vkey_url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey3428760851171131&\
g_tk=5381&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0\
&data=%7B%22req%22%3A%7B%22module%22%3A%22CDN.SrfCdnDispatchServer%22%2C%22method%22%3A%22\
GetCdnDispatch%22%2C%22param%22%3A%7B%22guid%22%3A%228871739380%22%2C%22calltype%22%3A0%2C%22\
userip%22%3A%22%22%7D%7D%2C%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22\
method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%228871739380%22%2C%22\
songmid%22%3A%5B%22{}%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%220%22%2C%22\
loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A0%2C%22\
format%22%3A%22json%22%2C%22ct%22%3A24%2C%22cv%22%3A0%7D%7D'.format(song_mid)
        response = requests.get(vkey_url, headers=self.headers)
        response = response.json()
        vkey = response.get('req_0').get('data').get('midurlinfo')[0].get('vkey')
        song_url = 'http://116.199.2.146/amobile.music.tc.qq.com/C400{0}.m4a?\
guid=8871739380&vkey={1}&fromtag=66'.format(song_mid, vkey)
        if song_mid != 0 and vkey != 0:
            return song_url
