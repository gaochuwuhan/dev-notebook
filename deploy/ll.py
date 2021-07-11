'''
Author: your name
Date: 2021-06-20 20:36:18
LastEditTime: 2021-06-20 20:38:27
LastEditors: your name
Description: In User Settings Edit
FilePath: /dev-notebook/deploy/ll.py
'''
class CiliumL4:
  
  def __init__(self,namespace,ingress_ip):
    self.namespace=namespace
    self.ingress_ip=str(IPv4Interface(ingress_ip).network)
  
  def replace_l4data(self,data): #将下面的data=下面的l4_data
    """将返回的结果传到cilium post请求中的data"""
    data["metadata"]["namespace"]=self.namespace
    data["spec"]["ingress"][0]["fromCIDRSet"][0]["cidr"]=self.ingress_ip
    return data
  
    
l4_data={
  "apiVersion": "cilium.io/v2",
  "kind": "CiliumNetworkPolicy",
  "metadata": {
    "name": "energy-tmp",
    "namespace": "zta"
  },
  "spec": {
    "endpointSelector": {
      "matchLabels": {
        "name": "487bc3c4-5361-4c1b-b486-e15bdd4e2697"
      }
    },
    "ingress": [
      {
        "fromCIDRSet": [
          {
            "cidr": "192.168.88.65/32"
          }
        ]
      }
    ],
    "egress": [
      {
        "toCIDRSet": [
          {
            "cidr": "10.92.32.110/32"
          }
        ],
        "toPorts": [
          {
            "ports": [
              {
                "port": "1883"
              }
            ]
          }
        ]
      },
      {
        "toFQDNs": [
          {
            "matchName": "www.wudun.net"
          }
        ],
        "toPorts": [
          {
            "ports": [
              {
                "port": "443"
              }
            ]
          }
        ]
      }
    ]
  }
}
   


json

------
    def energy_tmp_l4policy(self):
        app_ip=PasstivePolicy.objects.get(id=1).conditions["children"][0]["value"]
        visitor_ip=VisitorPolicy.objects.get(id)