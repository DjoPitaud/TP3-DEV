import socket
import re
from sys import argv

def is_valid_domain(domain: str) -> bool:
    
    domain_pattern = re.compile(r"^[a-z0-9-]+\.[a-z]{2,}$")
    return bool(domain_pattern.match(domain))


if len(argv) < 2:
    print("Veuillez fournir un nom de domaine.")
else:
    arg = argv[1]
    
    
    if not is_valid_domain(arg):
        print("Nom de domaine non valide.")
    else:
        try:
        
            ip_address = socket.gethostbyname(arg)
            print(ip_address)
        except socket.gaierror:
            print("Erreur lors de la résolution du nom de domaine.")
