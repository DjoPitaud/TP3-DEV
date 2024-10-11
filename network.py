import os
import socket
import is_up
import get_ip
import lookup 
from sys import argv, exit


def main():
    if not argv[1]:
        print("You must input a command (ip, lookup, ping)")
        exit(1)

    subcommand = argv[1]

    match subcommand:
        case "ping":
            if not argv[2]:
                print("You must input an IP address.")
                exit(2)
            
            if not is_up.ip_valid(subcommand):
                print("Veuillez rentrer une ip valide.")
                exit(3)
            else: 
                response = os.system(f"ping -n 4 {subcommand} > NUL 2>&1")

                if response == 0:
                    print("UP !")
                else:
                    print("DOWN !")

        case "lookup":
            if not argv[2]:
                print("You must input a hostname.")
                exit(2)

            if not lookup.is_valid_domain(arg):
                print(f"nom de domaine valide.")
                exit(3)
            try:
                ip_address = socket.gethostbyname(arg)
                print(ip_address)
            except socket.gaierror:
                print("Erreur lors de la résolution du nom de domaine.")
                exit(4)

        case "ip":
            get_ip.getIp()

            
    
            

