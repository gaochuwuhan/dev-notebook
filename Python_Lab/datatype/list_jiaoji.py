'''
Author: your name
Date: 2021-06-17 22:57:27
LastEditTime: 2021-06-20 15:56:34
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /dev-notebook/Python_Lab/datatype/list_jiaoji.py
'''
# '''
# Author: your name
# Date: 2021-06-17 22:57:27
# LastEditTime: 2021-06-19 15:18:33
# LastEditors: Please set LastEditors
# Description: In User Settings Edit
# FilePath: /dev-notebook/Python_Lab/datatype/list_jiaoji.py
# '''
# a=[[1,2,3],[3,4,5],[3,6,1]]
# print(list(set.intersection(*map(set,a))))
                      
#         [{'ps_id': 1, 'wg_ips': ['10.66.66.22']},
#          {'ps_id': 7, 'wg_ips': ['10.66.66.22']}]

# [{'ps_id': 7, 'url': '/operateMonitore/.*', 'uuid': UUID('f743ed79-650e-45bd-a20a-28f5216c19bf'), 'host': '192.168.88.163', 'port': 80, 'wg_ips': []}, 
#  {'ps_id': 7, 'url': '/selfsecurity/.*', 'uuid': UUID('f743ed79-650e-45bd-a20a-28f5216c19bf'), 'host': '192.168.88.163', 'port': 80, 'wg_ips': []}, 
#  {'ps_id': 7, 'url': '/selfsecurity/.*', 'uuid': UUID('f743ed79-650e-45bd-a20a-28f5216c19bf'), 'host': '192.168.88.163', 'port': 80, 'wg_ips': ['10.66.66.22', '10.66.66.23', '10.66.66.123', '10.66.66.24', '10.66.66.122']}, 
#  {'ps_id': 7, 'url': '/selfsecurity/.*', 'uuid': UUID('f743ed79-650e-45bd-a20a-28f5216c19bf'), 'host': '192.168.88.163', 'port': 80, 'wg_ips': ['10.66.66.22']}, 
#  {'ps_id': 7, 'url': '/hr/.*', 'uuid': UUID('f743ed79-650e-45bd-a20a-28f5216c19bf'), 'host': '192.168.88.163', 'port': 80, 'wg_ips': ['10.66.66.22']}]

# {'ps_id': 7, 'url': '/selfsecurity/.*', 'uuid': UUID('f743ed79-650e-45bd-a20a-28f5216c19bf'), 'host': '192.168.88.163', 'port': 80, 'wg_ips': ['10.66.66.22']}
# {'ps_id': 7, 'url': '/selfsecurity/.*', 'uuid': UUID('f743ed79-650e-45bd-a20a-28f5216c19bf'), 'host': '192.168.88.163', 'port': 80, 'wg_ips': ['10.66.66.22']}
# {'ps_id': 7, 'url': '/hr/.*', 'uuid': UUID('f743ed79-650e-45bd-a20a-28f5216c19bf'), 'host': '192.168.88.163', 'port': 80, 'wg_ips': ['10.66.66.22']}



# [{'ps_id': 7, 'url': '/selfsecurity/.*', 'uuid': 'f743ed79-650e-45bd-a20a-28f5216c19bf', 'host': '192.168.88.163', 'port': 80, 'wg_ips': ['10.66.66.22'], 'excute': ['PUT', 'GET']},
#  {'ps_id': 7, 'url': '/hr/.*', 'uuid': 'f743ed79-650e-45bd-a20a-28f5216c19bf', 'host': '192.168.88.163', 'port': 80, 'wg_ips': ['10.66.66.22'], 'excute': ['PUT', 'GET']}]

# a=[]
# b=[6,7]
# c=[5]
# a.append(b)
# a.append(c)
# print(a)
# aa=list(set.intersection(*map(set,a)))
# print(aa)

list1 = [4]
list1=list(set(list1))
print(list1)