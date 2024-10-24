from re import compile
from psutil import net_if_addrs
from socket import AF_INET


def ip_valid(addr: str) -> bool:

    ip_pattern = compile(
        r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
        r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
        r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
        r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    )
    return bool(ip_pattern.match(addr))

def ip_exist(ip):
    
    nic_data = net_if_addrs()
    for nic_name in nic_data.keys():
        if nic_name == "Wi-Fi" or "enp0s8":
        
            for addr in nic_data[nic_name]:
                if addr.family == AF_INET:
                    address = addr.address
    if not ip == address:
        return False
    return True   
