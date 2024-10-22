from sys import exit as sysexit
import socket

def client():
    host = '192.168.56.102'  
    port = 13337               

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host, port))
        print(f"Connecté avec succès au serveur {host} sur le port {port}")
        msg = str(input('Que veux-tu envoyer au serveur ? '))

        if type(msg) is not str:
            raise TypeError("Ici on veut que des strings !")
        
        if not 'meo' or 'waf'  in msg:
            raise ValueError("Ici on veut que meo et waf !")
        
        s.sendall(msg.encode("UTF-8"))
        data = s.recv(1024).decode("UTF-8")
        if not data: sysexit(1)
                    

        
        print(f"Le serveur a répondu {repr(data)}")
        sysexit(0)
    except socket.error:
        print("Error Occured.")
        sysexit(2)
    s.close()

client()

