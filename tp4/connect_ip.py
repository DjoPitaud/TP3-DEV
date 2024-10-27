from sys import exit as sysexit

from parse import parse_arg
from verif_ip import ip_valid
from verif_ip import ip_exist


def connect_ip():

    ip = parse_arg()[0]

    if not ip_valid(ip) == True:
        print(
            f"ERROR -l argument invalide. L'adresse {ip} n'est pas une adresse IP valide."
        )
        sysexit(3)

    elif not ip_exist(ip) == True:
        print(
            f"ERROR -l argument invalide. L'adresse {ip} n'est pas l'une des adresses IP de cette machine."
        )
        sysexit(4)

    return ip
