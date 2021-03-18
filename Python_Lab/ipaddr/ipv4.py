from ipaddress import IPv4Network, IPv4Interface,IPv4Address

IP1=IPv4Address('192.168.0.0')
# print(IP1)
NET1='192.168.88.0'
subnet = IPv4Interface(NET1).network
print (subnet)