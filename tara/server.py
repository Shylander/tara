# -*- coding: utf-8 -*-
import zmq
from engine import Engine

# local imports
import conf

class Server:
    def __init__(self):
        self.socket = conf.get_response_socket()
        self.socket.bind(conf.get_socket_bind_address())
        self.engine = Engine()
        print "Engine is pointed to " + Engine.get_executable()

    def listen(self):
        print "Listening to client on " + conf.get_socket_bind_address() + " ..."
        while True:
            message = self.socket.recv()
            response = engine.perform(message)
            self.socket.send(response)
            print "Echo: " + response
