from sys import exit as sysexit
from os import path, makedirs 
import socket
import logging

from re_verif import verifier_msg


TEMP_DIR = "/tmp/bs_clientII"

LOG_FILE = path.join(TEMP_DIR, "client.log")


try:
    makedirs(TEMP_DIR, exist_ok=True)
except Exception:
    print("Erreur lors de la création du dossier temporaire.")
    sysexit(1)

RED = "\033[91m"
WHI = "\033[37m"
NC = "\033[0m"

logger = logging.getLogger("logs")
logger.setLevel(20)
console_handler = logging.StreamHandler()
console_handler.setLevel(40)
logger.addHandler(console_handler)

logging.addLevelName(logging.ERROR, f"{RED}ERROR{NC}")
logging.addLevelName(logging.INFO, f"{WHI}INFO{NC}")


file_handler = logging.FileHandler(
    "/tmp/bs_clientII/client.log", mode="a", encoding="utf-8"
)
logger.addHandler(file_handler)

formatter = logging.Formatter(
    "{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
)

formatter_console = logging.Formatter(
    "{levelname} - {message}",
    style="{",
    
)

console_handler.setFormatter(formatter_console)
file_handler.setFormatter(formatter)

def client():

    host = '192.168.56.102'  
    port = 13337         

      

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host, port))
        logger.info(f"Connecté avec succès au serveur {host} sur le port {port}")
        input_client = str(input('écris ton calcule ? '))

        if type(input_client) is not str:
            raise TypeError("Ici on veut que des strings !")
        
        elif verifier_msg(input_client) is False:
            raise ValueError("Ici on veut que meo et waf !")

        msg = input_client.encode("UTF-8")
        s.sendall(msg)
        send_msg = msg.decode("UTF-8")
        logger.info(f"Message envoyé au serveur <{host}> : <{send_msg}>")
        data = s.recv(1024).decode("UTF-8")
        if not data: sysexit(1)
                    

        
        logger.info(f"Le serveur a répondu {repr(data)}")
        sysexit(0)
    except socket.error:
        logger.error(f"Impossible de se connecter au serveur <{host}> sur le port <{port}>..")
        sysexit(2)
    

client()

