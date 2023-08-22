import pymysql
import time
class Connection:
    def __init__(self):
        self.ip = '127.0.0.1'
        self.user = 'guest'
        self.password = '1q2w3e4r'
        self.database = 'testdb'
        self.conn = pymysql.connect(host=self.ip, user = self.user, password = self.password, database = self.password, charset = 'utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
        print('DB 연결 완료')

    def insert(self):
        sql = ""
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for data in res:
            print(data)

    def __del__(self):
        self.conn.close()
        print('DB 연결 끊김')



def main():
    con = Connection()
    sql = 'create table student (id int not null auto_increment, name varchar(45), address varchar(45), kor int, eng int, math int, science int, primary key(id));'
    cur.execute(sql)
res = cur.fetchall()
for data in res:
    print(data)
conn.close()

if __name__ == '__main__':
    main()
