import os
import re
import psutil
import socket
from socket import AF_INET
from sys import argv

def getIp():
    
    nic_data = psutil.net_if_addrs()
    for nic_name in nic_data.keys():
        if nic_name == "Wi-Fi":
        
            for addr in nic_data[nic_name]:
                if addr.family == AF_INET:
                    address = addr.address
                    netmask = addr.netmask
    cidr = sum(bin(int(x)).count('1') for x in netmask.split('.'))
    nb_addr = 2^(32-cidr)
                
    print(f"{address}/{cidr}")
    print(f"{nb_addr} adresses")
    
getIp()

def ip_valid(ip: str) -> bool:
    
    ip_pattern = re.compile(r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
                            r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
                            r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
                            r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
    return bool(ip_pattern.match(ip))



ip_address = argv[1]
    
    
if not ip_valid(ip_address):
    print("Adresse IP non valide.")
else:
        
    response = os.system(f"ping -n 4 {ip_address}")
        
        
    if response == 0:
        print("UP !")
    else:
        print("DOWN !")

def is_valid_domain(domain: str) -> bool:
    
    domain_pattern = re.compile(r"^[a-z0-9-]+\.[a-z]{2,}$")
    return bool(domain_pattern.match(domain))


if len(argv) < 2:
    print("Veuillez fournir un nom de domaine.")
else:
    domain = argv[1]
    
    
    if not is_valid_domain(domain):
        print("Nom de domaine non valide.")
    else:
        try:
        
            ip_address = socket.gethostbyname(domain)
            print(ip_address)
        except socket.gaierror:
            print("Erreur lors de la résolution du nom de domaine.")