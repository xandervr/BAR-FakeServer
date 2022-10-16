import threading
from lib import bar_socket


class BarChat(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.socket = socket
        self.connected = False

    def run(self):
        while True:
            msg = bar_socket.receive_message(self.socket)
            print("%s", msg)
