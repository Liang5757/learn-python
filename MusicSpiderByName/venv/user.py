from src.parser import *
from src.download import *
from db_tools.dbcollector import *
from utils.tools import *

if __name__ == '__main__':
    while input("输入q退出爬取，其余键继续爬取：") != 'q':
        search_key = input('请输入您想查询的歌手或歌名: ')
        music_crawler = Parse()
        music_db = Musicbd()

        json = music_crawler.getPage(search_key)
        song_info_1 = music_crawler.getSongInfo(json)     # 用于打印迭代
        music_crawler.printInfo(song_info_1)               # 输出所有歌曲信息

        nums = getnum()
        for num in nums:
            song_info_2 = music_crawler.getSongInfo(json)  # 用于获得选择歌曲的迭代
            select_song = music_crawler.selectSong(song_info_2, num)        # 获得选择歌曲信息
            if music_db.selectData(select_song):        # 判断音乐是否已经下载
                down_url = music_crawler.getSongUrl(select_song)      # 获取下载url
                download_music(down_url, select_song)        # 下载歌曲
                music_db.insertData('song_info', select_song)       # 保存歌曲信息到数据库
    music_db.closeDb()