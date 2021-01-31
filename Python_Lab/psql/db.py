import psycopg2

class Opdb:
    def __init__(self,dbname,user,password,host,port):
        self.dbname="apiapp"
        self.user="apiapp"
        self.password="Password01!"
        self.host="192.168.88.163"
        self.port="5432"
        self.conn,self.cursor=self.doconn()
    def doconn(self):
        conn = psycopg2.connect(dbname=self.dbname, user=self.user,
                password=self.password, host=self.host, port=self.port)
        cur = conn.cursor()  
        return conn,cur
    def dosql(self,sql_str):
        self.cursor.execute(sql_str)
        res=self.cursor.fetchall()
        return res
    def close(self):
        self.conn.close()



 