from pyvim.connect import SmartConnectNoSSL

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


if __name__ == '__main__':
    ip = '192.168.88.13'
    user = 'Administrator@vsphere.local'
    password = 'Binqsoft01!'
    port = 443
    vm = VmManage(host=ip,
                  user=user,
                  password=password,
                  port=port, ssl=None)
    if vm.result:
        # 说明连接成功，可以使用vm.client等
        print('vm is connecting')
    else:
        print(vm.message)
