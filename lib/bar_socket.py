import socket


def craft_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return sock


def connect_socket(sock, server_address):
    sock.connect(server_address)


def send_message(sock, message):
    sock.sendall(message.encode())


def receive_message(sock):
    data = sock.recv(1024)
    buffer = data
    while data.decode()[-1] != '\n':
        data = sock.recv(1024)
        buffer += data
    return buffer[:-1].decode()
