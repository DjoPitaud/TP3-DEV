import argparse

import verif_port

def connect_port():

    parser = argparse.ArgumentParser(description="arguments de port")

    
    parser.add_argument(
        '-p', '--port', 
        type=int, 
        default=13337, 
        help='Spécifiez le numéro de port (entre 0 et 65535)'
    )

    
    args = parser.parse_args()
    port = args.port

    verif_port.port_valid(port)
    print(type(port))
    
connect_port()


