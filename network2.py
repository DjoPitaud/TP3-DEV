import os
import sys
from datetime import datetime
import is_up
import get_ip
import lookup
from sys import argv, exit


if sys.platform == 'win32':
    TEMP_DIR = os.getenv('APPDATA') + '/Local/Temp/network_tp3'
else:
    TEMP_DIR = '/tmp/network_tp3'


LOG_FILE = os.path.join(TEMP_DIR, 'network.log')


if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

def log_command(command, args=None, error=False):

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if error:
        log_entry = f'{timestamp} [ERROR] Command {command} called with bad arguments : {args}.\n'
    else:
        if args:
            log_entry = f'{timestamp} [INFO] Command {command} called successfully with argument {args}.\n'
        else:
            log_entry = f'{timestamp} [INFO] Command {command} called successfully.\n'

    
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(log_entry)

def main():
    if len(argv) < 2 or not argv[1]:
        print("You must input a command (ip, lookup, ping)")
        log_command("unknown", "No command provided", error=True)
        exit(1)

    subcommand = argv[1].lower()

    match subcommand:
        case "ping":
            if len(argv) < 3 or not argv[2]:
                print("You must input an IP address.")
                log_command("ping", "No IP address provided", error=True)
                exit(2)
            else:
                ip_address = argv[2]
                log_command("ping", ip_address)
                is_up.is_up(ip_address)  

        case "lookup":
            if len(argv) < 3 or not argv[2]:
                print("You must input a hostname.")
                log_command("lookup", "No hostname provided", error=True)
                exit(2)
            else:
                hostname = argv[2]
                log_command("lookup", hostname)
                lookup.lookup(hostname)  

        case "ip":
            log_command("ip")
            get_ip.getIp()

        case _:
            print("You must input a valid command (ip, lookup, ping)")
            log_command(subcommand, "Invalid command", error=True)
            exit(1)

if __name__ == "__main__":
    main()
