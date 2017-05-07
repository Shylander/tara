# -*- coding: utf-8 -*-
import click

from tara import Tara
from tara.engine import Engine

@click.group()
def main():
    pass

@main.command()
@click.option('--path', '-p', default=None, help='Path of the file to be executed server side')
def execute(path):
    Engine.create(path)

@main.command()
def show():
    print Engine.get_executable()

@main.command()
@click.option('--message', '-m', default=None, help='Message to be sent to executable to be processed')
def perform(message):
    engine = Engine()
    print engine.perform(message)

@main.command()
def server():
    tara = Tara()
    tara.listen()

@main.command()
@click.option('--message', '-m', default=None, help='Message to be sent to server to be processed')
def client(message):
    tara = Tara()
    return tara.send(message)
