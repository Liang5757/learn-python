import requests
from urllib.parse import urlencode
from lxml import etree
import re
import os
import time

from database.movie_db import *

# from multiprocessing.pool import Pool
# from multiprocessing import Queue

cookies = '''bid=pj5Huf8S-B8; douban-fav-remind=1; __utmc=30149280; ll="108258"; _\
vwo_uuid_v2=D19F9F22CE4E24CF4434E459BA227532F|fcbdf7f19c7bd3dfa0fb77b64666ac71; ct=y; \
OUTFOX_SEARCH_USER_ID_NCOO=1810275428.6919246; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1557571905\
%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1834068780.1554\
282311.1557451380.1557571908.23; __utmz=30149280.1557571908.23.9.utmcsr=google|utmccn=(organic)|utm\
cmd=organic|utmctr=(not%20provided); __utmt=1; dbcl2="186363991:4OfMN/CV7AM"; ck=K8dc; _pk_id.10000\
1.8cb4=fce3a99e71b5ef9d.1554282310.5.1557571927.1557164021.; push_noty_num=0; push_doumail_num=0; __\
utmv=30149280.18636; __utmb=30149280.3.10.1557571908'''
jar = requests.cookies.RequestsCookieJar()
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)

# 获取带爬取的url
class UrlSpider(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/52.0.2743.116 Safari/537.36'
        }
        # 用以储存待爬url
        self.movie_url = []
        # 爬取的页面始末位置
        self.START = 99
        self.END = 100

    def getPage(self, start):
        params = {
            'sort': 'U',
            'range': '0,10',
            'tags': '',
            'start': start,
        }
        base_url = 'https://movie.douban.com/j/new_search_subjects?' + urlencode(params)
        try:
            response = requests.get(base_url, cookies=jar, headers=self.headers)
            if response.status_code == 200:
                return response.json()
        except requests.ConnectionError:
            return None

    def getMovieUrl(self, json):
        if json.get('data'):
            for item in json.get('data'):
                url = item.get('url')
                self.movie_url.append(url)

    def getUrlMain(self):
        for start in [x * 20 for x in range(self.START, self.END + 1)]:
            json = self.getPage(start)
            self.getMovieUrl(json)
        return self.movie_url

# 获取电影详细信息
class MovieSpider(object):
    def __init__(self, url):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/52.0.2743.116 Safari/537.36'
        }
        self.movie_detail_url = url

    def getPage(self):
        try:
            response = requests.get(self.movie_detail_url, cookies=jar, headers=self.headers)
            html = etree.HTML(response.text)
            return html
        except requests.ConnectionError:
            return None

    def parse(self):
        # 存放电影信息
        movie_detail = {}
        html = self.getPage()
        # 电影名
        moviename = html.xpath('//*[@id="content"]/h1/span[1]/text()')[0].split(' ', 1)
        movie_detail['moviename'] = moviename[0]
        movie_detail['englishname'] = None if len(moviename) == 1 else moviename[1]
        director = html.xpath('//*[@id="celebrities"]/ul/li[1]/div/span[1]/a/text()')
        movie_detail['director'] = director[0] if director else None
        star = html.xpath('//*[@id="celebrities"]/ul/li[2]/div/span[1]/a/text()')
        movie_detail['star'] = star[0] if star else None
        # 电影类型
        movie_type = html.xpath('//*[@id="info"]/span[@property="v:genre"]/text()')
        type_len = len(movie_type)
        for i in range(3):
            if i < type_len:
                movie_detail['type{}'.format(i + 1)] = movie_type[i]
            else:
                movie_detail['type{}'.format(i + 1)] = 'None'
        # 制片国家
        release_date = html.xpath('//*[@id="info"]/span[@property="v:initialReleaseDate"]/@content')
        if release_date:
            movie_detail['place'] = None
        else:
            place_search = re.search('([\u4E00-\u9FA5]+)', release_date)
            movie_detail['place'] = place_search.group(1) if place_search else None
        # 电影评分
        movie_score = html.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
        movie_detail['score'] = movie_score[0] if movie_score else 0
        # 电影上映时间
        movie_detail['years'] = html.xpath('//*[@id="content"]/h1/span[2]/text()')[0].replace('(', '').replace(')', '')
        # 剧情简介
        introduction = html.xpath('//*[@id="link-report"]/span[contains(@property, "v:summary") or \
                                    contains(@class, "all hidden")]/text()')
        introduction = ''.join(''.join(introduction).split())
        movie_detail['introduction'] = introduction
        # 时长
        timelong = html.xpath('//*[@id="info"]/span[@property="v:runtime"]/@content')
        timelong = timelong[0] if timelong else None
        movie_detail['timelong'] = timelong
        # 详情网址
        movie_detail['link'] = self.movie_detail_url
        movie_detail['img_url'] = html.xpath('//*[@id="mainpic"]/a/img/@src')[0]

        return movie_detail

# 下载图片
def downloadImg(movie_detial, last_id):
    img_path = os.path.dirname(os.getcwd()) + os.path.sep + 'src' + os.path.sep + '电影图片'
    print(img_path)
    if not os.path.exists(img_path):
        os.mkdir(img_path)
    try:
        url = movie_detial['img_url']
        response = requests.get(url)
        if response.status_code == 200:
            picture_file_name = last_id + 1
            file_path = img_path + os.path.sep + '{0}.{1}'.format(picture_file_name, 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print('下载成功')
            else:
                print('本地存在该图片!')
    except requests.ConnectionError:
        print('下载图片失败！！！')


if __name__ == '__main__':
    movie_urls = UrlSpider().getUrlMain()
    movie_db = MovieDb()
    for movie_url in movie_urls:
        name = MovieSpider(movie_url).parse()
        movie_db.insertData('movie_qg', name)
        last_id = movie_db.getLastId()
        movie_db.updatePicture(last_id)
        downloadImg(name, last_id)
        time.sleep(0.01)
    movie_db.closedb()