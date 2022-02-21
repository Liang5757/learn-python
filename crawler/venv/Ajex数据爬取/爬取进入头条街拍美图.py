## 导入需要的包
import json
import os
import time
from hashlib import md5
from urllib.parse import urlencode
import re
import requests
from bs4 import BeautifulSoup

from requests.exceptions import RequestException


def validatetile(title):
    """
    :param title: 传入的参数
    :return: 将无法作为标题的符号替换为_
    """
    rstr = '[/\:*?<>|@]'
    new_title = re.sub(rstr, '_', title)
    return new_title


def get_page_index(offset):
    """
    :param offset: Ajax 网页每次的偏移值
    :return:输出每次刷新出来的网页
    """
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': 1
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
        'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D'
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页出错')
        return None


def parse_one_index(html):
    """
    :param html: 获取到的网页信息
    :return: 一个字典，包含标题和一个图片网址列表
    """
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            title = item.get('title')
            if 'image_list' in item.keys() and item['image_list'] != []:
                images = item.get('image_list')
                imgs = []
                for image in images:
                    imgs.append(image.get('url').replace('list/190x124', 'origin').replace('list', 'origin'))

                yield {
                    'title': title,
                    'image_urls': imgs
                }


def save_image(item):
    if not os.path.exists(validatetile(item.get('title'))):
        os.mkdir(validatetile(item.get('title')))
        try:
            for image_url in item.get('image_urls'):
                response = requests.get(image_url)
                if response.status_code == 200:
                    file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
                    if not os.path.exists(file_path):
                        with open(file_path, 'wb') as f:
                            f.write(response.content)
                        print('Downloaded image path is:', file_path)
                    else:
                        print('Already Downloaded', file_path)
        except requests.ConnectionError:
            print('Failed to Save Image')


def main():
    for i in range(3):
        print(f'正在爬取offset为{i * 20}')
        html = get_page_index(i * 20)
        print(html)
        for item in parse_one_index(html):
            save_image(item)
        time.sleep(5)


if __name__ == '__main__':
    main()
