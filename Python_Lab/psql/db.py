import psycopg2

# from logging.logger import logger
class Opdb:
    def __init__(self,dbname,user,password,host,port):
        self.dbname=dbname
        self.user=user
        self.password=password
        self.host=host
        self.port=port
        self.conn,self.cursor=self.doconn()
    def doconn(self):
        conn = psycopg2.connect(dbname=self.dbname, user=self.user,
                password=self.password, host=self.host, port=self.port)
        cur = conn.cursor()  
        return conn,cur
    def fetchall(self,sql_str):
        self.cursor.execute(sql_str)
        res=self.cursor.fetchall()
        return res  #返回一个list，list中的每个元素是一个元祖，元祖里面是一行dict数据，可以这样记，一张表有多行是可以重复的所以最外面是list；一行字段不能重复，所以用元祖；字段和值一一映射所以用dict
    def fetchone(self,sql_str):
        self.cursor.execute(sql_str)
        count=self.cursor.fetchone()
        return count

    def close(self):
        self.conn.close()