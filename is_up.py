import os
import re
from sys import argv

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
