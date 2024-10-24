import argparse
from sys import exit as sysexit

from verif_port import port_valid
from verif_port import port_private


def connect_port():

    parser = argparse.ArgumentParser(description="arguments de port")

    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=13337,
        help="usage: [file] [option] [argument] \n -p, --port Spécifiez le numéro de port (entre 0 et 65535)",
    )

    args = parser.parse_args()

    if not port_valid(args.port) == True:
        print(
            "ERROR -p argument invalide. Le port spécifié <PORT> n'est pas un port valide (de 0 à 65535)."
        )
        sysexit(1)

    elif not port_private(args.port) == True:
        print(
            "ERROR -p argument invalide. Le port spécifié <PORT> est un port privilégié. Spécifiez un port au dessus de 1024."
        )
        sysexit(2)

    port = args.port

    return port


connect_port()
