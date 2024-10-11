import psutil
from socket import AF_INET


def getNetworkInfo():
    
    nic_data = psutil.net_if_addrs()
    for nic_name in nic_data.keys():
        if not nic_name == "Wi-Fi":
        
            for addr in nic_data[nic_name]:
                if addr.family == AF_INET:
                    address = addr.address
                    netmask = addr.netmask
    cidr = sum(bin(int(x)).count('1') for x in netmask.split('.'))
                
    print(f"{address}/{cidr}")
    
getNetworkInfo()

