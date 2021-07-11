from ipaddress import IPv4Network, IPv4Interface,IPv4Address
host1="www.baidu.com"
host2="192.168.88.1"
IP1=IPv4Address(host2)
IP2=IPv4Address(host1)
print(IP1,type(IP1),IP2)
# NET1='192.168.88.99'
# subnet = str(IPv4Interface(NET1).network)
# print (subnet,type(subnet))