import psycopg2
import ipaddress
from ipaddress import IPv4Address, IPv4Network
from db import Opdb

'''针对api_probe表的测试: 每个方法对应一个语句以及想返回的结果'''
class All_probe:
    
    con_db=Opdb(dbname="apiapp",user="apiapp",password="Password01!",host="192.168.88.163",port="5432")
    def get_all(self):
        q_sql=("select row_to_json(api_probe) from api_probe")
        res_all=self.con_db.fetchall(q_sql)
        item1 = [item[0] for item in res_all]
        # 等价于
        # item1=[]
        # for item in res_all:
        #     item1.append(item[0])
        return item1
    
    def get_count(self):
        q_sql=("select count(1) from api_probe")
        res = self.con_db.fetchone(q_sql)[0] #为了返回int，不加 [0]是一个元组
        return res

    def get_multi(self):
        q_sql=("select row_to_json(api_probe) from api_probe LIMIT 50 OFFSET 0")
        res=self.con_db.fetchall(q_sql)
        list_=[item[0] for item in res]
        count=self.get_count()
        return list_,count


# print(All_probe().get_multi()) #将All_probe的get_all方法实现的功能结果直接打印
    

    # def get_subnets_probe_ip_map(get_dict):
    #     return {
    #         ipaddress.ip_network(subnet): probe["ip_manage"]
    #         for probe in get_dict
    #         for subnet in probe["subnets"]
    #     } 

    # print(get_subnets_probe_ip_map(get_dict=get_dict))



 