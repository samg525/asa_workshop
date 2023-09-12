#! /usr/bin/env python
"""
Set up for mymodule
"""
from setuptools import setup

import os

def get_requirements():
    """
    Read the requirements from a file
    """
    requirements = []
    if os.path.exists('requirements.txt'):
        with open('requirements.txt') as req:
            for line in req:
                # skip commented lines
                if not line.startswith('#'):
                    requirements.append(line.strip())
    return requirements

# requirements = ['numpy>=1.0',
#                 # others
#                 ]

setup(
    name='mymodule', # the name of the module
    packages=['mymodule'], # the location of the module
    version="0.1",
    # install_requires=requirements,
    install_requires=get_requirements(),
    python_requires='>=3.8',
    entry_points={
        'console_scripts':[
            'hello_world=mymodule.submod1:hello_world',
            'sky_sim=mymodule.sky_sim:main',
            ]}
)
