import is_up
import get_ip
import lookup 
from sys import argv, exit


def main():
    
    if not argv[1]:
        print("You must input a command (ip, lookup, ping)")
        exit(1)

    subcommand = argv[1].lower()
    

    match subcommand:
        case "ping":
            if not argv[2]:
                print("You must input an IP address.")
                exit(2)
            else:
                
                is_up.is_up()

        case "lookup":
            if not argv[2]:
                print("You must input a hostname.")
                exit(2)
            else:

                lookup.lookup()

        case "ip":
            get_ip.getIp()
        
        case _:
            print("You must input a command (ip, lookup, ping)")
            exit(1)

if __name__ == "__main__":
    main()
            

