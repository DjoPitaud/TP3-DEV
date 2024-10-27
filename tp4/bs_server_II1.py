import socket
from sys import exit as sysexit
import logging
import time

from reponse import repondre
from connect_ip import connect_ip
from connect_port import connect_port

jaune = "\033[33m"
blanc = "\033[37m"
reset = "\033[0m"

logger = logging.getLogger("logs")
logger.setLevel(20)
console_handler = logging.StreamHandler()  
logger.addHandler(console_handler)

logging.addLevelName(logging.WARNING, f"{jaune}WARN{reset}")
logging.addLevelName(logging.INFO, f"{blanc}INFO{reset}")


file_handler = logging.FileHandler("/var/log/bs_server/bs_server.log", mode="a", encoding="utf-8")
logger.addHandler(file_handler)

formatter = logging.Formatter(
    "{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M:%S",
)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)


def main():

    host = connect_ip()
    port = connect_port()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((host, port))

    s.listen(1)
    
    logger.info(f"Le serveur tourne sur {host}:{port}")


    conn, addr = s.accept()
    logger.info(f"Un client {addr[0]} s'est connecté.")

    while True:

        try:

            data = conn.recv(1024).decode("UTF-8")
            start_time = time.time()
            fin_timer = 60 

            if not data:
                passed_time = time.time() - start_time
                if passed_time >= fin_timer:
                    logger.warning("Aucun client depuis plus d'une minute.")
                    start_time = time.time()
                sysexit(1)
                
            
            logger.info(f"Le client {addr[0]} a envoyé "f"{data}"".")

            conn.sendall(repondre(data))
            send_msg = repondre(data).decode("UTF-8")

            logger.info(f"Réponse envoyée au client <{addr[0]} : "f"{send_msg}"".")

            s.close()

            
        except socket.error:
            print("Error Occured.")
            sysexit(2)


if __name__ == "__main__":
    main()
