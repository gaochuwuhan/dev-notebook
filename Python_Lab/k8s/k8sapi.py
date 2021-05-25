from kubernetes import client,config
from config import settings
import sys

# sys.path.append('/Users/apple/github/dev-notebook/Python_Lab')
print(sys.path)

ApiToken = settings.K8S_API_KEY
configuration = client.Configuration()
setattr(configuration, 'verify_ssl', False)
client.Configuration.set_default(configuration)
configuration.host = settings.K8S_API_SERVER    #ApiHost
configuration.verify_ssl = False
configuration.debug = True
configuration.api_key = {"authorization": "Bearer " + ApiToken}
client.Configuration.set_default(configuration)

k8s_api_obj  = client.CoreV1Api(client.ApiClient(configuration))
ret = k8s_api_obj.list_namespaced_ciliumnetworkpolicies.cilium.io("nexus-ng1-pc")
print(ret)

