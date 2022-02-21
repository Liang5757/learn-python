import pymysql


class Musicbd(object):
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='123', port=3306, db='spiders')
        self.cursor = self.db.cursor()

    # 为用户建表
    def creatTable(self, table_name):
        sql = '''CREATE TABLE IF NOT EXISTS {} (
                    song_mid VARCHAR(255) NOT NULL,
                    song_name VARCHAR(255) NOT NULL,
                    singer_name VARCHAR(255) NOT NULL,
                    song_time VARCHAR(255) NOT NULL,
                    PRIMARY KEY (song_mid)
                    )'''.format(table_name)
        self.cursor.execute(sql)

    # 插入数据
    def insertData(self, table, song_info):
        data = {
            'song_mid': song_info['song_mid'],
            'song_name': song_info['song_name'],
            'singer_name': '/'.join(song_info['singer_name']),
            'song_time': song_info['song_time'],
        }
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
        try:
            if self.cursor.execute(sql, tuple(data.values())):
                print('成功插入数据')
                self.db.commit()
        except:
            print('插入数据失败')
            self.db.rollback()

    # 查询数据
    def selectData(self, song_info):
        sql = "SELECT * FROM song_info WHERE song_mid = '{}' LIMIT 1".format(song_info['song_mid'])
        try:
            self.cursor.execute(sql)
            one = self.cursor.fetchone()     # 获取结果的第一条数据
            if one:
                print('在数据库中查询到该音乐：', one)
                return False
            else:
                return True
        except:
            print('ERROR')
            return False

    # 关闭数据库
    def closeDb(self):
        self.db.close()

