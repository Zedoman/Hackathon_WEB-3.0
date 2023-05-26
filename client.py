import socket
import tqdm


def File_Client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    client.bind((host, port))
    client.listen()

    server, addr = client.accept()
    print("Connected to :{}".format(addr))

    file_name = server.recv(1024).decode()
    print("FILE NAME :{}".format(file_name))

    file_size = server.recv(1024).decode()
    print("FILE SIZE :{} Kb".format(file_size))

    file = open(file_name, "wb")

    file_bytes = b""

    done = False
    progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=int(file_size))

    while not done:
        data = server.recv(1024)
        if file_bytes[-5:] == b"<END>":
            done = True
        else:
            file_bytes += data
        progress.update(1024)
    file.write(file_bytes)
    file.close()
    server.close()
    client.close()
