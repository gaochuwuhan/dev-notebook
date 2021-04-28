import psycopg2
import ipaddress
from ipaddress import IPv4Address, IPv4Network
from db import Opdb


q_sql=("select row_to_json(api_probe) from api_probe")
res_all=Opdb(dbname="apiapp",user="apiapp",password="Password01!",host="192.168.88.163",port="5432").dosql(q_sql)
print(res_all)


# def get_all(res_all):
#     # print(type(res_all))
#     item1 = [item[0] for item in res_all]
#     # x=[]
#     # for item in res_all:
#     #     x.append(item[0])
#     # print(type(item1))
#     # print("=============")
#     # x=[]  x[{},{}]
#     # for i in res_all:
#     #     x.append(i[0])
#     return item1

# get_dict=get_all(res_all=res_all)

# def get_subnets_probe_ip_map(get_dict):
#     return {
#         ipaddress.ip_network(subnet): probe["ip_manage"]
#         for probe in get_dict
#         for subnet in probe["subnets"]
#     } 

# print(get_subnets_probe_ip_map(get_dict=get_dict))



 