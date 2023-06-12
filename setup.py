import ast
import re

import setuptools

setuptools.setup(
    name = "saludo",
    version = '0.1',
    description = 'Prueba de libreria de saludo',
    url = 'https://github.com/Carlos676/saludo',
    author = 'Carlos',
    author_email = 'juancarlosemp600a@gmail.com',
    license = 'MIT',
    packages = ['saludo'],
    
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent', 
    ],
    zip_safe = False,
)