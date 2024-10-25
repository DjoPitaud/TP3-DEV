from sys import exit as sysexit
import socket

from reponse import repondre


def main():

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

            conn.sendall(repondre(data))

            s.close()

        except socket.error:
            print("Error Occured.")
            sysexit(2)


if __name__ == "__main__":
    main()
# 8.70/10 pylint
