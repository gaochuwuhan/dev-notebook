
import psycopg2
import ipaddress
from ipaddress import IPv4Address, IPv4Network
from db import Opdb

class All_ipassets:
    con_db=Opdb(dbname="apiapp",user="apiapp",password="Password01!",host="127.0.0.1",port="5432")
    def get_id(self,id):
        q_sql = f"select row_to_json(api_ipassets) from api_ipassets where id = %s"
        cursor = self.con_db.cursor
        cursor.execute(q_sql,[id])
        res = cursor.fetchone()
        return res[0] if res else None

print(All_ipassets().get_id(2203)['ip_address'])