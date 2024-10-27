import logging

ok = "ok"
nop = "nop"

def logs_server(arg1, arg2):

    jaune = "\033[33m"
    blanc = "\033[37m"
    reset = "\033[0m"

    logger = logging.getLogger("logs")
    logger.setLevel(20)
    console_handler = logging.StreamHandler()  
    logger.addHandler(console_handler)
    
    logging.addLevelName(logging.WARNING, f"{jaune}WARN{reset}")
    logging.addLevelName(logging.INFO, f"{blanc}INFO{reset}")

    
    #file_handler = logging.FileHandler("/var/log/bs_server/bs_server.log", mode="a", encoding="utf-8")
    #logger.addHandler(file_handler)

    formatter = logging.Formatter(
        "{asctime} - {levelname} - {message}",
         style="{",
         datefmt="%Y-%m-%d %H:%M:%S",
    )
    
    console_handler.setFormatter(formatter)
    
    

    i_serveur= f"Le serveur tourne sur {arg1}:{arg2}"
    i_connect = f"Un client {arg1} s'est connecté."
    i_reciv = f"Le client {arg1} a envoyé {arg2}."
    i_send = f"Réponse envoyée au client {arg1} : {arg2}."
    no_client = "Aucun client depuis plus de une minute."

    
    logger.info(i_serveur)
    logger.info(i_connect)
    logger.info(i_reciv)
    logger.info(i_send)
    logger.warning(no_client)

    

logs_server(ok, nop)
