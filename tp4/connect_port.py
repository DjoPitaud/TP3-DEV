from sys import exit as sysexit

from parse import parse_arg
from verif_port import port_valid
from verif_port import port_private


def connect_port():

    port = parse_arg()[1]

    if not port_valid(port) == True:
        print(
            "ERROR -p argument invalide. Le port spécifié <PORT> n'est pas un port valide (de 0 à 65535)."
        )
        sysexit(1)

    elif not port_private(port) == True:
        print(
            "ERROR -p argument invalide. Le port spécifié <PORT> est un port privilégié. Spécifiez un port au dessus de 1024."
        )
        sysexit(2)

    return port
