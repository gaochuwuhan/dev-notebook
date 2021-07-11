"""
Author: your name
Date: 2021-06-12 14:54:40
LastEditTime: 2021-06-12 17:36:26
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /dev-notebook/Python_Lab/k8s/replace_value.py
"""
from request import Request

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

example_service = {
  "metadata": {
    "name": "f743ed79-650e-45bd-a20a-28f5216c19bf", 
    "labels": {
      "name": "f743ed79-650e-45bd-a20a-28f5216c19bf", 
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
      "name": "f743ed79-650e-45bd-a20a-28f5216c19bf"
    }
  },
  "apiVersion": "v1",
  "kind": "Service"
}

service_data = {
  "metadata": {
    "name": "wudun-web", 
    "namespace": "wuddun-608",
    "labels": {
      "name": "wudun-web"
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
      "name": "wudun-web"
    }
  },
  "apiVersion": "v1",
  "kind": "Service"
}


class DataOp:
    """将返回的客体set传入"""
    def __init__(self,namespace,uuid,host,port):
        self.namespace = namespace
        self.uuid = uuid
        self.host = host
        self.port = port
        
        
    def replace_deployment(self,data):
        data["metadata"]["name"]=self.uuid 
        data["metadata"]["namespace"]=self.namespace
        data["metadata"]["labels"]["name"]=self.uuid 
        data["spec"]["template"]["metadata"]["labels"]["name"]=self.uuid 
        data["spec"]["template"]["spec"]["containers"][0]["env"][0]["value"]=self.host
        data["spec"]["template"]["spec"]["containers"][0]["env"][1]["value"]=str(self.port)
        data["spec"]["selector"]["matchLabels"]["name"]=self.uuid 
        return data
    
    def replace_service(self,data):
        data["metadata"]["name"]=self.uuid 
        data["metadata"]["namespace"]=self.namespace
        data["metadata"]["labels"]["name"]=self.uuid
        data["spec"]["selector"]["name"]=self.uuid
        return data
    
data = DataOp(namespace="wudun-608",uuid="f743ed79-650e-45bd-a20a-28f5216c19bfb",port="443",host="www.baidu.com").replace_service(data=service_data)
print(data)

print(Request(path="/api/v1/namespaces/wudun-608/services").post(data=data))
        
        
