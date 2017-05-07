# -*- coding: utf-8 -*-
import os
import imp

# local imports
import conf

class Engine():
    @classmethod
    def present(cls, filepath=conf.ENGINE_FILE):
        return os.path.isfile(filepath)

    @classmethod
    def create(cls, filepath):
        if Engine.present(filepath):
            Engine.safe_remove(conf.ENGINE_FILE)
            target = open(conf.ENGINE_FILE, 'w+')
            target.write(filepath)
            print "Added " + filepath + " to " + conf.ENGINE_FILE
        else:
            raise FileNotFoundError(filepath + "file not found")

    @classmethod
    def safe_remove(cls, filepath=conf.ENGINE_FILE):
        if Engine.present(filepath):
            os.remove(filepath)

    @classmethod
    def get_executable(cls):
        target = open(conf.ENGINE_FILE, 'r+')
        return target.readline()

    def __init__(self):
        if not Engine.present():
            raise ValueError("conf (" + conf.ENGINE_FILE + ") file not found")
        elif not Engine.present(Engine.get_executable()):
            raise ValueError("executable (" + Engine.get_executable() + ") file not found")

        # TODO: For Python 3+, http://stackoverflow.com/a/67692/2572999
        self.executable = imp.load_source('module.name', Engine.get_executable())

    def perform(self, message):
        return self.executable.perform(message)
