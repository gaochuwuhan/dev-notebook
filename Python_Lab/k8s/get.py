from request import headers
from config import settings
import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# from logging.logger import logger

requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #取消ssl不安全警告

path = "/api/v1/namespaces/ng1"
url = f"{settings.K8S_API_SERVER}{path}"
# logger.info(url)
print(url,headers)

res=requests.get(url=url,headers=headers,verify=False)

serve-probe:
        cd netprobe/deploy && docker-compose -f docker-compose.activation.yml up -d
serve-ds-kafka:
        cd plat/ds && docker-compose  -f docker-compose_kafka.yml --env-file plat.env up -d
serve-ds-elk:
        cd plat/ds && docker-compose  -f docker-compose_elk.yml --env-file plat.env up -d
serve-ds-api:
        cd plat/ds && docker-compose  -f docker-compose_deploy.yml --env-file plat.env up -d

stop-ap:
        docker-compose -f docker-compose.ap.yml -p hgongy down
stop-probe:
        cd netprobe/deploy && docker-compose -f docker-compose.activation.yml down
stop-ds:
        cd plat && docker-compose  -f docker-compose_kafka.yml down && docker-compose  -f docker-compose_elk.yml down && docker-compose  -f docker-compose_deploy.yml down