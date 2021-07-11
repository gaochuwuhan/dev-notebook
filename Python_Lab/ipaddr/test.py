'''
Author: your name
Date: 2021-06-19 22:11:27
LastEditTime: 2021-06-19 22:16:37
LastEditors: Please set LastEditors
Description: In User Settings Edi
FilePath: /dev-notebook/Python_Lab/ipaddr/test.py
'''
from ipaddress import IPv4Network, IPv4Interface,IPv4Address

class CiliumDataOp:
  
    def __init__(self, namespace, policy_list):
        self.namespace = namespace
        self.uuid = policy_list['uuid']
        self.host = str(IPv4Interface(policy_list['host']).network) #要判断段是ip还是fqdn，ip要把子网掩码写上
        self.port = str(policy_list['port'])
        self.url = policy_list['url']
        self.cilium_name= policy_list['cilium_name']
        self.excute = policy_list['excute']
        self.wg_ips = policy_list['wg_ips']
        self.valid_ips=[]
        for ip in self.wg_ips:
          wg_ip=str(IPv4Interface(ip).network)
          self.valid_ips.append(wg_ip)
    
    def ip(self):
        return self.valid_ips
    
print(CiliumDataOp(namespace="wudun-608",policy_list={
      "ps_id": 7,
      "url": "/selfsecurity/.*",
      "uuid": "f743ed79-650e-45bd-a20a-28f5216c19bf",
      "host": "192.168.88.163",
      "port": 80,
      "wg_ips": [
        "10.66.66.123",
        "10.66.66.22"
      ],
      "excute": [
        "PUT",
        "GET"
      ],
      "cilium_name": "selfsecurity-f743ed79-650e-45bd-a20a-28f5216c19bf"
    }).ip())
          
    