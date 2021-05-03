import psycopg2
import ipaddress
from ipaddress import IPv4Address, IPv4Network
from db import Opdb

class All_device:
    con_db=Opdb(dbname="apiapp",user="apiapp",password="Password01!",host="192.168.88.163",port="5432")
    def get_id(self,id):
        q_sql = f"select row_to_json(api_device) from api_device where id = %s"
        cursor = self.con_db.cursor
        cursor.execute(q_sql,[id])
        res = cursor.fetchone()
        return res[0] if res else None

# print(All_device().get_id([2,3]))