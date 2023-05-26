import os
import socket


# random generation of code encoding --- 45 ---- 45
def File_Server(file_name):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999

    server.connect((host, port))

    file = open(file_name, 'rb')
    server.send("Received.png".encode())

    file_size = os.path.getsize(file_name)
    server.send((str(file_size)).encode())

    data = file.read()
    server.sendall(data)
    server.send(b"<END>")

    file.close()
    server.close()
