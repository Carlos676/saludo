import ast
import re

import setuptools

readme=open(".README.md","r")
setuptools.setup(
    name = "saludo",
    packages = ['saludo'],
    version = '0.1',
    description = 'Prueba de libreria de saludo',
    long_description=readme.read(),
    long_description_contenr_type='text/markdown',
    author = 'Carlos',
    author_email = 'juancarlosemp600a@gmail.com',
    url = 'https://github.com/Carlos676/saludo',
    license = 'MIT',    
    classifiers = [
        'Prueba de libreria',
        ],
    include_package_data=TR,
)
