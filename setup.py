# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='bot',
    version='0.0.2',
    description='Turn any Python file into a service',
    author='Swaathi Kakarla',
    url = 'https://github.com/skcript/tara',
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': [
            'tara = tara.cli:main',
        ],
    },
    install_requires=(
    	['zmq']
    )
)
