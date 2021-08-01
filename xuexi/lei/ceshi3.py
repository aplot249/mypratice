import pymysql

class Mydata:
    def __init__(self):
        self.db_info = {
            'db':"mysql",
            'password':"qq1788lover",
            'user':"root",
            'port':3306
        }
        self.connector = pymysql.connect(**self.db_info)

    def __enter__(self):
        print("已经进入！")
        return self.connector

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("结束完毕，进行输出")
        self.connector.close()

with Mydata() as mydata:
    cursor = mydata.cursor()
    cursor.execute('show tables;')
    for i in cursor.fetchall():
        print(i)


