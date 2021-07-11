import IPy
from websockets.exceptions import ConnectionClosed

def  is_ip(address):
    try:
        IPy.IP(address)
        return True
    except Exception as  e:
        return False
    
print(is_ip("192.168.88.1"))