from os import getenv, path, makedirs
from datetime import datetime
from sys import argv, exit as sysexit, platform

import is_up
import get_ip
import lookup

if platform == "win32":
    temp_dir = getenv("TEMP")
    if not temp_dir:
        print("La variable d'environnement 'TEMP' n'est pas définie.")
        sysexit(1)
    TEMP_DIR = path.join(temp_dir, "network_tp3")
else:
    TEMP_DIR = "/tmp/network_tp3"

LOG_FILE = path.join(TEMP_DIR, "network.log")


try:
    makedirs(TEMP_DIR, exist_ok=True)
except Exception:
    print("Erreur lors de la création du dossier temporaire.")
    sysexit(1)


def log_command(command, args=None, error=False):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if error:
        log_entry = f"{timestamp} [ERROR] Command {command} called with bad arguments : {args}\n"
    else:
        if args:
            log_entry = f"{timestamp} [INFO] Command {command} called successfully with argument {args}\n"
        else:
            log_entry = f"{timestamp} [INFO] Command {command} called successfully.\n"

    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_entry)


def main():

    if not argv[1]:
        print("You must input a command (ip, lookup, ping)")
        sysexit(1)

    subcommand = argv[1].lower()

    match subcommand:
        case "ping":
            if not argv[2]:
                print("You must input an IP address.")
                sysexit(2)
            else:

                is_up.is_up()
                log_command("ping", argv[2])

        case "lookup":
            if not argv[2]:
                print("You must input a hostname.")
                sysexit(2)
            else:

                lookup.lookup()
                log_command("lookup", argv[2])

        case "ip":
            get_ip.getIp()
            log_command("ip")

        case _:
            print("You must input a command (ip, lookup, ping)")
            sysexit(1)


if __name__ == "__main__":
    main()
