'''
Author: your name
Date: 2021-05-16 21:13:35
LastEditTime: 2021-06-16 11:34:22
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /dev-notebook/Python_Lab/k8s/ciliumapi.py
'''
import requests
from config import settings
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #取消ssl不安全警告


'''用普通的request请求去对k8s api进行操作'''
ApiToken = settings.K8S_API_KEY
headers = {"authorization": "Bearer " + ApiToken,
            "Content-Type": "application/json"}
path = "/apis/cilium.io/v2/namespaces/ng1/ciliumnetworkpolicies/nexus-ng1-pc"
path1 = "/apis/cilium.io/v2/namespaces/ng1/ciliumnetworkpolicies"
url = f"{settings.K8S_API_SERVER}{path1}"
# data = 'ingress': [{'fromCIDRSet': [{'cidr': '192.168.88.65/32'}]}]}
res = print(requests.get(url=url,headers=headers,verify=False).json())

# class CiliumRequest:
#     # def __init__(self)
#     def get_policy(self):   
#         print(res.ok)
#         policy = res.json()
#         return policy
    
    # def patch_policy(self):


# print(get_policy())
# cur_ingress=CiliumRequest().get_policy()['spec']['ingress']
# print(cur_ingress)

# def patch_policy():
#     res = requests.patch(url=url,headers=headers,json=)