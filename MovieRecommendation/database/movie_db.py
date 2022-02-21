import pymysql


class MovieDb(object):
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='123', port=3306, db='movie')
        self.cursor = self.db.cursor()

    # 为用户建表
    def creatTable(self):
        sql = '''CREATE TABLE IF NOT EXISTS `movie_qg` (
          `ID` int(20) NOT NULL AUTO_INCREMENT,
          `moviename` varchar(50) DEFAULT NULL,
          `englishname` varchar(50) DEFAULT NULL,
          `dataID` int(20) DEFAULT NULL,
          `director` varchar(50) DEFAULT NULL,
          `star` varchar(50) DEFAULT NULL,
          `type1` varchar(30) DEFAULT NULL,
          `type2` varchar(30) DEFAULT NULL,
          `type3` varchar(30) DEFAULT NULL,
          `picture` varchar(500) DEFAULT NULL,
          `place` varchar(50) DEFAULT NULL,
          `score` float DEFAULT NULL,
          `years` int(20) DEFAULT NULL,
          `introduction` varchar(1000) DEFAULT NULL,
          `timelong` int(20) DEFAULT NULL,
          `link` varchar(200) DEFAULT NULL,
          PRIMARY KEY (`ID`)
        ) ENGINE=InnoDB AUTO_INCREMENT=9986 DEFAULT CHARSET=utf8mb4;'''
        self.cursor.execute(sql)

    # 插入数据
    def insertData(self, table, movie_detail=None):
        data = {
            'moviename': movie_detail['moviename'],
            'englishname': movie_detail['englishname'],
            'director': movie_detail['director'],
            'star': movie_detail['star'],
            'type1': movie_detail['type1'],
            'type2': movie_detail['type2'],
            'type3': movie_detail['type3'],
            'place': movie_detail['place'],
            'score': movie_detail['score'],
            'years': movie_detail['years'],
            'introduction': movie_detail['introduction'],
            'timelong': movie_detail['timelong'],
            'link': movie_detail['link'],
            # 待添加
            'dataID': None,
            'picture': '',
        }
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
        try:
            if self.cursor.execute(sql, tuple(data.values())):
                print('成功插入数据')
                self.db.commit()
        except Exception as e:
            print(e)
            print('插入数据失败')
            self.db.rollback()

    # 查询电影信息
    def selectData(self, movie_name):
        sql = "SELECT * FROM movie_qg WHERE moviename = '{}'".format(movie_name)
        try:
            self.cursor.execute(sql)
            one = self.cursor.fetchone()  # 获取结果的第一条数据
            if one:
                print('在数据库中查询到该电影：', one)
                return True
            else:
                return False
        except Exception as e:
            # print(e)
            return False

    # 获取最后插入的id
    def getLastId(self):
        sql = 'SELECT max(ID) FROM movie_qg'
        try:
            self.cursor.execute(sql)
            last_id = self.cursor.fetchone()[0]
            return last_id
        except Exception as e:
            print(e)
            return False

    # 更新图片名
    def updatePicture(self, last_id):
        sql = "UPDATE movie_qg SET picture='%s' WHERE id = %d;" % (str(last_id)+'.jpg', last_id)
        try:
            self.cursor.execute(sql)
            return True
        except Exception as e:
            print(e)
            return False

    # 插入数据
    def insertUser(self, table, recommend=None):
        data = {
            'id': recommend[0],
            'movieId1': None,
            'movieId2': None,
            'movieId3': None,
        }
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
        try:
            if self.cursor.execute(sql, tuple(data.values())):
                print('成功插入数据')
                self.db.commit()
        except Exception as e:
            print(e)
            print('插入数据失败')
            self.db.rollback()

    # 查询电影id
    def selectMovieId(self, user_id):
        sql = "SELECT * FROM users WHERE ID = '{}'".format(user_id)
        try:
            self.cursor.execute(sql)
            one = self.cursor.fetchone()
            if one:
                print('在数据库中查询到该电影：', one)
                return False
            else:
                return True
        except Exception as e:
            # print(e)
            return False

    # 关闭数据库
    def closedb(self):
        self.db.close()
