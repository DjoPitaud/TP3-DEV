# TP3 DEV : Premiers pas Python



## Sommaire

- [TP3 DEV : Premiers pas Python](#tp3-dev--premiers-pas-python)
  - [Sommaire](#sommaire)
- [I. Ping](#i-ping)
- [II. DNS](#ii-dns)
- [III. Get your IP](#iii-get-your-ip)
- [IV. Mix](#iv-mix)
- [V. Logs](#v-logs)
- [VI. Deploy](#vi-deploy)

# I. Ping

🌞 **`ping_simple.py`**

- importez la fonction `system` de la lib `os`
- utilisez-la pour effectuer un `ping 8.8.8.8`
``` 
import os
 
ping = 'ping 8.8.8.8'

os.system(ping);
```

---


🌞 **`ping_arg.py`**

- importez la liste `argv` de la lib `sys`
  - cette liste contient les arguments passés au script à l'exécution
- effectuez un `ping` vers l'IP fournie en argument quand on exécute le code

```
import os
from sys import argv

ip_address = argv[1]
print(f"Exécution du ping vers {ip_address}...")
    
response = os.system(f"ping -n 2 {ip_address}") 
```

🌞 **`is_up.py`**

- même code que `ping_arg.py` mais il doit
  - soit juste afficher "UP !" si la machine répond au ping
  - soit juste afficher "DOWN !" si la machine ne répond pas
  - vous ne devez donc PAS afficher le ping en cours, uniquement `UP !` ou `DOWN !`
- vous devez vérifier que l'argument saisi a bien le format d'une adresse IP

```
import os
import re
from sys import argv, platform

def ip_valid(addr: str) -> bool:
    
    ip_pattern = re.compile(r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
                            r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
                            r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
                            r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
    return bool(ip_pattern.match(addr))

    
def is_up(): 

    subcommand = argv[1]  
    
    if not ip_valid(subcommand):
        print("Adresse IP non valide.")
        exit(3)
    else:
        
    response = os.system(f"ping -n 1 -w 50 {subcommand} > NUL 2>&1")
        
        if response == 0:
            print("UP!")
        else:
            print("DOWN!") 

is_up()
```

# II. DNS

🌞 **`lookup.py`**

```
import socket
import re
from sys import argv, exit

def is_valid_domain(domain: str) -> bool:
    
    domain_pattern = re.compile(r"^[a-z0-9-]+\.[a-z]{2,}$")
    return bool(domain_pattern.match(domain))

def lookup():
    
    subcommand = argv[1]
        
        
    if not is_valid_domain(subcommand):
        print("Nom de domaine non valide.")
        exit(3)
    else:
        try:
            
            ip_address = socket.gethostbyname(subcommand)
            print(ip_address)
        except socket.gaierror:
            print("Erreur lors de la résolution du nom de domaine.")
            exit(4)

lookup()
```

# III. Get your IP

🌞 **`get_ip.py`**

- utilisez la fonction `net_if_addrs()` de la librairie `psutil` par exemple
- votre code doit afficher l'adresse IP de votre carte WiFi
- à partir du masque de sous-réseau, calculer et afficher le nombre d'adresses IP dispo dans le réseau

```
import psutil
from socket import AF_INET


def getIp():
    
    nic_data = psutil.net_if_addrs()
    for nic_name in nic_data.keys():
        if nic_name == "Wi-Fi":
        
            for addr in nic_data[nic_name]:
                if addr.family == AF_INET:
                    address = addr.address
                    masque_r = addr.netmask
    cidr = sum(bin(int(x)).count('1') for x in masque_r.split('.'))
    nb_addr = 2^(32-cidr)
                
    print(f"{address}/{cidr}")
    print(f"{nb_addr} adresses")

get_ip()
```

# IV. Mix

🌞 **`network.py`**

- doit contenir une fonction `lookup()` qui prend en argument un nom de domaine et retourne l'IP qui correspond
- doit contenir une fonction `ping()` qui prend en argument une IP et retourne "UP !" ou "DOWN !"
- doit contenir une fonction `ip()` qui prend rien en argument et retourne l'IP de la carte WiFi + nombre IP dispos dans le réseau
- **ne doit contenir qu'un seul `print()`**
- ça doit donner ça :

```
from os import getenv
from sys import argv, exit as sysexit, platform

import is_up
import get_ip
import lookup

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
            

        case "lookup":
            if not argv[2]:
                print("You must input a hostname.")
                sysexit(2)
            else:

                lookup.lookup()
                

        case "ip":
            get_ip.getIp()
            

        case _:
            print("You must input a command (ip, lookup, ping)")
            sysexit(1)


if __name__ == "__main__":
    main()
```


# V. Logs

🌞 **Continuez sur le script précédent `network.py`**

```
from os import getenv, path, makedirs
from datetime import datetime
from sys import argv, exit as sysexit, platform

import is_up
import get_ip
import lookup


temp_dir = getenv("TEMP")
    if not temp_dir:
        print("La variable d'environnement 'TEMP' n'est pas définie.")
        sysexit(1)
TEMP_DIR = path.join(temp_dir, "network_tp3")


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
```

# VI. Deploy

🌞 **Déployez-moi ça dans une VM Rocky**

```
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

    if subcommand == "ping":
        if not argv[2]:
            print("You must input an IP address.")
            sysexit(2)
        else:
            is_up.is_up()
            log_command("ping", argv[2])

    elif subcommand == "lookup":
        if not argv[2]:
            print("You must input a hostname.")
            sysexit(2)
        else:
            lookup.lookup()
            log_command("lookup", argv[2])

    elif subcommand == "ip":
        get_ip.getIp()
        log_command("ip")

    else:
        print("You must input a command (ip, lookup, ping)")
        sysexit(1)


if __name__ == "__main__":
    main()
```
## Module `get_ip.py` modification:
```
nic_data = psutil.net_if_addrs()
    for nic_name in nic_data.keys():
        if nic_name == "Wi-Fi" or "enp0s8":
```
## Module `is_up.py` modification:
```
else:
        if platform == "win32":
            response = os.system(f"ping -n 1 -w 500 {subcommand} > NUL 2>&1")
        else:
            response = os.system(f"ping -c 1 {subcommand} > NUL 2>&1")
```