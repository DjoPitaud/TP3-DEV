from sys import exit as sysexit
import socket


def server():

    host = '' 
    port = 13337 


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((host, port))  


    s.listen(1)

    conn, addr = s.accept()

    print('Connected by', addr)


    while True:

        try:
            
            data = conn.recv(1024)

        
            if not data: sysexit(1)

            
            print(f"Données reçues du client : {data}")

            
            conn.sendall("Hi mate!".encode("UTF-8"))
            sysexit(0)

        except socket.error:
            print("Error Occured.")
            sysexit(2)


    conn.close()

server()