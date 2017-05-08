# local imports
import conf
from server import Server

class Tara:
    def listen(self):
        Server().listen()

    def send(self, message):
        client = conf.get_request_socket()
        client.connect(conf.get_socket_connect_address())
        client.send(message)

        return client.recv()
