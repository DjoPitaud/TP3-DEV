from sys import exit as sysexit
import socket

import reponse


def server():

    host = ""
    port = 13337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((host, port))

    s.listen(1)

    conn, addr = s.accept()

    print(f"Un client vient de se co et son IP c'est {addr[0]}")

    while True:

        try:

            data = conn.recv(1024).decode("UTF-8")

            if not data:
                sysexit(1)

            print(f"Données reçues du client : {data}")

            conn.sendall(reponse.repondre(data))

            s.close()

        except socket.error:
            print("Error Occured.")
            sysexit(2)


server()
