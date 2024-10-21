from sys import exit as sysexit
import socket

def repondre(message):
    if "meo" in message.lower():
        return "Meo à toi confrère.".encode("UTF-8")
    elif "waf" in message.lower():
        return "ptdr t ki".encode("UTF-8")
    else:
        return "Mes respects humble humain.".encode("UTF-8")
    
def server():

    host = '' 
    port = 13337 


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((host, port))  


    s.listen(1)

    conn, addr = s.accept()

    print(f"Un client vient de se co et son IP c'est {addr}.")


    while True:

        try:
            
            data = conn.recv(1024)

        
            if not data: sysexit(1)

            
            print(f"Données reçues du client : {data}")

            
            conn.sendall(repondre(data))
            sysexit(0)

        except socket.error:
            print("Error Occured.")
            sysexit(2)


server()