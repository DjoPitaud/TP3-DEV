import argparse
from sys import exit as sysexit

from verif_ip import ip_valid
from verif_ip import ip_exist

def connect_ip():

    parser_ip = argparse.ArgumentParser(description="arguments d'ip")

    parser_ip.add_argument(
        "-l",
        "--listen",
        help="usage: [file] [option] [argument] \n -l, --listen  Spécifiez l'ip ",
    )

    args = parser_ip.parse_args()

    if not ip_valid(args.listen) == True:
        print("ERROR -l argument invalide. L'adresse <ADRESSE> n'est pas une adresse IP valide.")
        sysexit(3)

    elif not ip_exist(args.listen) == True:
        print("ERROR -l argument invalide. L'adresse <ADRESSE> n'est pas l'une des adresses IP de cette machine.")
        sysexit(4)

    host = args.listen
    
    return host
