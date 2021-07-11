import json-patch

deployment_data = {
    "type": "apps.deployment",
    "metadata": {
        "namespace": "wudun-608", #先写死
        "annotations": {
            "field.cattle.io/description": "中台8001接口代理"
        },
        "name": "plat-api", #去查 ，先写uuid
        "labels": {
            "name": "object_uuid", 
            "wudun_id": "e7d9e125-732a-4849-b135-73f082ff8ef5" #去查 ，先写uuid
        }
    },
    "spec": {
        "replicas": 1,
        "selector": {
            "matchLabels": {
                "name": "plat-api" #去查 ，先写uuid
            }
        },
        "template": {
            "metadata": {
                "labels": {
                    "name": "plat-api" #去查 ，先写uuid
                }
            },
            "spec": {
                "restartPolicy": "Always",
                "containers": [
                    {
                        "name": "nginx_proxy_wudun", #如果pod只有一个容器可以写死
                        "imagePullPolicy": "Always", #如果对方能提供在线仓库，否则填 IfNotPresent
                        "image": "dockerhub.qingcloud.com/zta_project/nginx_proxy_wudun:1.0",
                        "ports": [
                            {
                                "name": "http",
                                "protocol": "TCP",
                                "containerPort": "去查"
                            }
                        ],
                        "env": [
                            {
                                "name": "PROXY_HOST",
                                "value": "去查客体host"
                            },
                            {
                                "name": "PROXY_PORT",
                                "value": "去查客体port"
                            },
                            {
                                "name": "LISTEN_PORT",
                                "value": "8001" #写死
                            }
                        ]
                    }
                ],
                "imagePullSecrets": [
                    {
                        "name": "qingcloud" #对方的仓库
                    }
                ]
            }
        }
    }
}

