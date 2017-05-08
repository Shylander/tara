# -*- coding: utf-8 -*-
import os
import zmq

home = os.path.expanduser("~")
context = zmq.Context()

ENGINE_FILE = os.path.join(home, ".tara.config")
SOCKET_BIND_ADDRESS = "tcp://*:1625"
SOCKET_CONNECT_ADDRESS = "tcp://127.0.0.1:1625"

def get_socket_bind_address():
    get_env_var("BIND_ADDR", SOCKET_BIND_ADDRESS)

def get_socket_connect_address():
    get_env_var("CONNECT_ADDR", SOCKET_CONNECT_ADDRESS)

def get_response_socket():
    return context.socket(zmq.REP)

def get_request_socket():
    return context.socket(zmq.REQ)

def get_env_var(var, default):
    try:
        env_var = os.environ[var]
        return env_var
    except:
        return default
