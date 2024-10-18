import psutil
from socket import AF_INET


def getIp():
    
    nic_data = psutil.net_if_addrs()
    for nic_name in nic_data.keys():
        if nic_name == "Wi-Fi" or "enp0s8":
        
            for addr in nic_data[nic_name]:
                if addr.family == AF_INET:
                    address = addr.address
                    masque_r = addr.netmask
    cidr = sum(bin(int(x)).count('1') for x in masque_r.split('.'))
    nb_addr = 2^(32-cidr)
                
    print(f"{address}/{cidr}")
    print(f"{nb_addr} adresses")
    
