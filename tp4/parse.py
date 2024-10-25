import argparse


def parse_arg():
    parser = argparse.ArgumentParser(description="arguments d'ip")

    parser.add_argument(
        "-l",
        "--listen",
        help="usage: [file] [option] [argument] \n -l, --listen  Spécifiez l'ip ",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=13337,
        help="usage: [file] [option] [argument] \n -p, --port Spécifiez le numéro de port (entre 0 et 65535)",
    )
    args = parser.parse_args()
    ip = args.listen
    port = args.port
    arguments = (ip, port)

    return arguments
