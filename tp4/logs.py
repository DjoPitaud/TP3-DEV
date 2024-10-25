import logging

def logs_server():
    logger = logging.getLogger(__name__)
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("/var/log/bs_server/bs_server.log", mode="a", encoding="utf-8")
    console_handler.setLevel(20)
    file_handler.setLevel(20)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    formatter_console = logging.Formatter(
        "{asctime} - {levelname} - {message}",
         style="{",
         datefmt="%Y-%m-%d %H:%M:%S",
    )
    
