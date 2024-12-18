import socket
import re
from sys import argv, exit

def is_valid_domain(domain: str) -> bool:
    
    domain_pattern = re.compile(r"^[a-z0-9-]+\.[a-z]{2,}$")
    return bool(domain_pattern.match(domain))

def lookup():
    
    subcommand = argv[2]
        
        
    if not is_valid_domain(subcommand):
        print("Nom de domaine non valide.")
        exit(3)
    else:
        try:
            
            ip_address = socket.gethostbyname(subcommand)
            print(ip_address)
        except socket.gaierror:
            print("Erreur lors de la résolution du nom de domaine.")
            exit(4)
