from config import settings
import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #取消ssl不安全警告


# ApiToken = settings.K8S_API_KEY
# headers = {"authorization": "Bearer " + ApiToken,
#             "Content-Type": "application/json-patch+json"} #content-type要是json-type patch方法才会生效

class Request:
    def get_headers(self):
        ApiToken = settings.K8S_API_KEY
        headers = {"authorization": "Bearer " + ApiToken,
            "Content-Type": "application/json"}
        return headers

    def __init__(self,path):
      #/api/v1/namespaces/wudun-608/services
        self.headers=self.get_headers()
        self.path=path
        self.url=settings.K8S_API_SERVER + self.path

    def get(self):
        res = requests.get(url=self.url,headers=self.headers,verify=False)
        if res.ok:
            content = res.json()
            return content
        return res.status_code

    def post(self,data):
        res=requests.post(url=self.url,headers=self.headers,verify=False,json=data)
        if res.ok:
            content = res.json()
            return content
        return res.text

    def patch(self,data):
        res=requests.patch(url=self.url,headers=self.headers,verify=False,json=data)
        if res.ok:
            content = res.json()
            return content
        return res.status_code
    def delete(self):
        res = requests.delete(url=self.url,headers=self.headers,verify=False)
        if res.ok:
            content = res.json()
            return content
        return res.status_code




# print(Request(path="/api/v1/namespaces/ng1/services/my-ng1").get())

# data=[
#     {
#         "op": "replace",
#         "path": "/spec/ingress/0/fromCIDRSet/0/cidr",
#         "value": "192.168.88.140/32"
#     }
# ]
cilium_data = {
  "apiVersion": "cilium.io/v2",
  "kind": "CiliumNetworkPolicy",
  "metadata": {
    "name": "nexus-ng1-pc",
    "namespace": "ng1"
  },
  "spec": {
    "endpointSelector": {
      "matchLabels": {
        "name": "nexus-ng1"
      }
    },
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
                "port": "4200"
              }
            ]
          }
        ]
      },
      {
        "toEndpoints": [
          {
            "matchLabels": {
              "io.kubernetes.pod.namespace": "kube-system",
              "k8s-app": "kube-dns"
            }
          }
        ],
        "toPorts": [
          {
            "ports": [
              {
                "port": "53",
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

deployment_data = {
  "metadata": {
    "name": "f743ed79-650e-45bd-a20a-28f5216c19bf",
    "namespace": "wudun-608",
    "labels": {
      "name": "f743ed79-650e-45bd-a20a-28f5216c19bf"
    },
    "annotations": {
      "io.cilium.proxy-visibility": "<Egress/80/TCP/HTTP>"
    }
  },
  "spec": {
    "template": {
      "metadata": {
        "labels": {
          "name": "f743ed79-650e-45bd-a20a-28f5216c19bf"
        }
      },
      "spec": {
        "imagePullSecrets": [
          {
            "name": "qingcloud"
          }
        ],
        "containers": [
          {
            "name": "nginx",
            "env": [
              {
                "name": "PROXY_HOST",
                "value": "192.168.88.163"
              },
              {
                "name": "PROXY_PORT",
                "value": "80"
              },
              {
                "name": "LISTEN_PORT",
                "value": "8380"
              }
            ],
            "ports": [
              {
                "containerPort": 8380
              }
            ],
            "image": "dockerhub.qingcloud.com/zta_project/nginx_proxy_wudun:1.0",
            "imagePullPolicy": "IfNotPresent"
          }
        ]
      }
    },
    "selector": {
      "matchLabels": {
        "name": "f743ed79-650e-45bd-a20a-28f5216c19bf"
      }
    },
    "replicas": 1
  },
  "type": "apps.deployment"
}

service_data={
  "metadata": {
    "name": "1165a9f-ceb5-40ec-97e4-7a289ce1582b", 
    "namespace": "wudun-608",
    "labels": {
      "name": "1165a9f-ceb5-40ec-97e4-7a289ce1582b"
    }
  },
  "spec": {
    "ports": [
      {
        "name": "http", 
        "port": 8380, 
        "targetPort": 8380,
      }
    ],
    "type": "NodePort",
    "externalTrafficPolicy": "Local",
    "selector": {
      "name": "1165a9f-ceb5-40ec-97e4-7a289ce1582b"
    }
  },
  "apiVersion": "v1",
  "kind": "Service"
}

dep_data=
{'metadata': {'name': '9663fae5-85b5-4626-ac78-adfa2d7e2a8e', 'namespace': 'wudun-608', 'labels': {'name': '9663fae5-85b5-4626-ac78-adfa2d7e2a8e'}, 'annotations': {'io.cilium.proxy-visibility': '<Egress/80/TCP/HTTP>'}}, 'spec': {'template': {'metadata': {'labels': {'name': '9663fae5-85b5-4626-ac78-adfa2d7e2a8e'}}, 'spec': {'imagePullSecrets': [{'name': 'qingcloud'}], 'containers': [{'name': 'nginx', 'env': [{'name': 'PROXY_HOST', 'value': 'www.wudun.net'}, {'name': 'PROXY_PORT', 'value': '443'}, {'name': 'LISTEN_PORT', 'value': '8380'}], 'ports': [{'containerPort': 8380}], 'image': 'dockerhub.qingcloud.com/zta_project/nginx_proxy_wudun:1.0', 'imagePullPolicy': 'IfNotPresent'}]}}, 'selector': {'matchLabels': {'name': '9663fae5-85b5-4626-ac78-adfa2d7e2a8e'}}, 'replicas': 1}, 'type': 'apps.deployment'}
{'metadata': {'name': '8f679b25-58d4-4f1d-bfa5-7c52169b3f69', 'namespace': 'wudun-608', 'labels': {'name': '8f679b25-58d4-4f1d-bfa5-7c52169b3f69'}, 'annotations': {'io.cilium.proxy-visibility': '<Egress/80/TCP/HTTP>'}}, 'spec': {'template': {'metadata': {'labels': {'name': '8f679b25-58d4-4f1d-bfa5-7c52169b3f69'}}, 'spec': {'imagePullSecrets': [{'name': 'qingcloud'}], 'containers': [{'name': 'nginx', 'env': [{'name': 'PROXY_HOST', 'value': 'www.aws.com'}, {'name': 'PROXY_PORT', 'value': 443}, {'name': 'LISTEN_PORT', 'value': '8380'}], 'ports': [{'containerPort': 8380}], 'image': 'dockerhub.qingcloud.com/zta_project/nginx_proxy_wudun:1.0', 'imagePullPolicy': 'IfNotPresent'}]}}, 'selector': {'matchLabels': {'name': '8f679b25-58d4-4f1d-bfa5-7c52169b3f69'}}, 'replicas': 1}, 'type': 'apps.deployment'}
# print(Request(headers=headers,path="/apis/cilium.io/v2/namespaces/ng1").post(data=data))

# print(Request(path="/apis/cilium.io/v2/namespaces/ng1/ciliumnetworkpolicies/nexus-ng1-pc").get())
# print(Request(path="/apis/apps/v1/namespaces/wudun-608/deployments").post(dep_data))

print(Request(path="/api/v1/namespaces/wudun-608/services").post(service_data))
      