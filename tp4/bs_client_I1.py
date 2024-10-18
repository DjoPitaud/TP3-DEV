import socket

def client():
    host = '192.168.56.102'  
    port = 13337               


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    s.connect((host, port))



    s.sendall(b'SALUT MEC')


    data = s.recv(1024)


    s.close()


    print(f"Le serveur a répondu {repr(data)}")

client()

