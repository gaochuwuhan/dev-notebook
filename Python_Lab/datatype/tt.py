'''
Author: your name
Date: 2021-06-19 20:40:04
LastEditTime: 2021-06-19 21:07:41
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /dev-notebook/Python_Lab/datatype/tt.py
'''
class CiliumDataOp:
  
  def __init__(self, namespace, policy_list):
        self.namespace = namespace
        self.uuid = policy_list['uuid']
        self.host = policy_list['host'] #要判断段是ip还是fqdn
        self.port = str(policy_list['port'])
        self.url = policy_list['url']
        self.cilium_name= policy_list['cilium_name']
        self.excute = policy_list['excute']
        self.ingress_ip = policy_list['wg_ips']
  
  def replace_metadata(self,data): #将calculate_cilium_policy方法计算后的多个列表传入生成多个cilium json文件
      data["metadata"]["name"]=self.cilium_name
      data["metadata"]["namespace"]=self.namespace
      data["spec"]["egress"][0]["toCIDRSet"][0]["cidr"]=self.host
      data["spec"]["egress"][0]["toPorts"][0]["ports"][0]["port"]=self.port
      
      return data
    
  def replace_rules(self,data):
    """
    如果一个url set有多个http方法被允许需要将["rules"]["http"]列表放多个url和方法的字典，
    列表中字典形式: {
                  "method": "GET",
                  "path": "/assetVisualization/.*"
                }
    """
    http_rules=[]
    excute_counts=len(self.excute) #得到一个url规则被允许的方法个数
    for ex in range(0,excute_counts):
      http_rules.append({"method": self.excute[ex], "path": self.url})
    data["spec"]["egress"][0]["toPorts"][0]["rules"]["http"]=http_rules
    return data
  
  def replace_ingress(self,data):
    """如果有等多个wg ip,["spec"]["igress"]就是由多个fromCIDRSet组成的列表
        {
        "fromCIDRSet": [
          {
            "cidr": "192.168.88.65/32"
          }
        ]
        },
    
    """
    
    ingress_sets=[]
    ingress_counts=len(self.ingress_ip)
    for ex in range(0,ingress_counts):
      ingress_sets.append({"fromCIDRSet": [
          {
            "cidr": self.ingress_ip[ex]
          }
        ]
      })
    data["spec"]["ingress"] = ingress_sets
    print('*'*80,f"{ingress_sets}")
    return data
    
  def get_clium_data(self,data):
    temp_data=self.replace_rules(data=self.replace_metadata(data=data))
    cilium_data=self.replace_ingress(data=temp_data)
    print(f"得到cilium json是：{cilium_data}")
    return cilium_data

policy_list={
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
    }
      
cilium_data = {
  "apiVersion": "cilium.io/v2",
  "kind": "CiliumNetworkPolicy",
  "metadata": {
    "name": "selfsecurity-f743ed79-650e-45bd-a20a-28f5216c19bf",
    "namespace": "wudun-608"
  },
  "spec": {
    "egress": [
      {
        "toCIDRSet": [
          {
            "cidr": "192.168.88.163/32"
          }
        ],
        "toPorts": [
          {
            "ports": [
              {
                "port": "80",
                "protocol": "TCP"
              }
            ],
            "rules": {
              "http": [
                {
                  "method": "GET",
                  "path": "/assetVisualization/.*"
                }
              ]
            }
          }
        ]
      },
      {
        "toFQDNs": [
          {
            "matchName": "ds.wudun.net"
          }
        ],
        "toPorts": [
          {
            "ports": [
              {
                "port": "8001",
                "protocol": "TCP"
              }
            ]
          }
        ]
      },
      {
        "toEndpoints": [
          {
            "matchLabels": {
              "k8s:io.kubernetes.pod.namespace": "kube-system",
              "k8s:k8s-app": "kube-dns"
            }
          }
        ],
        "toPorts": [
          {
            "ports": [
              {
                "port": "53",
                "protocol": "ANY"
              }
            ],
            "rules": {
              "dns": [
                {
                  "matchPattern": "*"
                }
              ]
            }
          }
        ]
      },
      {
        "toEndpoints": [
          {
            "matchLabels": {
              "k8s:dns.operator.openshift.io/daemonset-dns": "default",
              "k8s:io.kubernetes.pod.namespace": "openshift-dns"
            }
          }
        ],
        "toPorts": [
          {
            "ports": [
              {
                "port": "5353",
                "protocol": "UDP"
              }
            ],
            "rules": {
              "dns": [
                {
                  "matchPattern": "*"
                }
              ]
            }
          }
        ]
      }
    ],
    "endpointSelector": {
      "matchLabels": {
        "name": "f743ed79-650e-45bd-a20a-28f5216c19bf"
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
    ]
  }
}
      
print(CiliumDataOp(namespace="wudun-608",policy_list=policy_list).get_clium_data(data=cilium_data))