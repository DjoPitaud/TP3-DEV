from sys import exit as sysexit
import socket

def client():
    host = '192.168.56.102'  
    port = 13337               

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    s.sendall("Meooooo !".encode("UTF-8"))
    data = s.recv(1024)
    if not data: sysexit(1)
                  

    
    print(f"Le serveur a répondu {repr(data)}")
    sysexit(0)
    

client()

