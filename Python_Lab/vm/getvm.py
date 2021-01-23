from pyvim.connect import SmartConnectNoSSL
from pyVmomi import *


class VmManage(object):

    def __init__(self, host, user, password, port, ssl):
        self.host = host
        self.user = user
        self.pwd = password
        self.port = port
        self.sslContext = ssl
        try:
            self.client = SmartConnectNoSSL(host=host,
                                            user=user,
                                            pwd=password,
                                            port=443
                                            )
            self.content = self.client.RetrieveContent()
            self.result = True
        except Exception as e:
            self.result = False
            self.message = e
    def _get_all_objs(self, obj_type, folder=None):
        """
        根据对象类型获取这一类型的所有对象
        """
        if folder is None:
            container = self.content.viewManager.CreateContainerView(self.content.rootFolder, obj_type, True)
        else:
            container = self.content.viewManager.CreateContainerView(folder, obj_type, True)
        return container.view


    def _get_obj(self, obj_type, name):
        """
        根据对象类型和名称来获取具体对象
        """
        obj = None
        content = self.client.RetrieveContent()
        container = content.viewManager.CreateContainerView(content.rootFolder, obj_type, True)
        for c in container.view:
            if c.name == name:
                obj = c
                break
        return obj

    def get_datacenters(self):
        """
       返回所有的数据中心
        """
        return self._get_all_objs([vim.Datacenter])


    def get_datacenter_by_name(self, datacenter_name):
        """
       根据数据中心名称获取数据中心对象
        """
        return self._get_all_objs([vim.Datacenter], datacenter_name)

'''
tiaoshi

'''
if __name__ == '__main__':
    ip = '192.168.88.13'
    user = 'Administrator@vsphere.local'
    password = 'Binqsoft01'
    port = 443
    vm = VmManage(host=ip,
                  user=user,
                  password=password,
                  port=port, ssl=None)
    cluster_objs = vm._get_all_objs([vim.ClusterComputeResource])
    print (cluster_objs)
