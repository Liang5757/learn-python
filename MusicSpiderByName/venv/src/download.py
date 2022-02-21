import os
import requests

# 下载音乐
def download_music(url, song_info):
    song_path = 'music'
    if not os.path.exists(song_path):
        os.mkdir(song_path)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            singer_name = '&'.join(song_info['singer_name'])
            singer_name = singer_name.replace(" ", "")      # 去空格
            file_name = song_info['song_name'] + '_' + singer_name + '_' + song_info['song_mid']
            file_path = song_path + os.path.sep + '{0}.{1}'.format(file_name, 'mp4')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print('下载成功')
            else:
                print('本地存在该音频文件!')
    except requests.ConnectionError:
        print('下载音乐失败！！！')



