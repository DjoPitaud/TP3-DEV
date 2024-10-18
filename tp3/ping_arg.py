import os
from sys import argv

ip_address = argv[1]
print(f"Exécution du ping vers {ip_address}...")
    
response = os.system(f"ping -n 2 {ip_address}")  



