#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from codecs import open

from setuptools import find_packages, setup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read(*paths):
    """Build a file path from *paths and return the contents."""
    with open(os.path.join(*paths), 'r', 'utf-8') as f:
        return f.read()

requires = [
    'Pillow==3.1.1',
    'pygame==1.9.1release',
    'tornado==4.3',
    'ws4py==0.3.4'
]

entry_points = {}

extras_require = {}


setup(
    name='burningkingdoms',
    version='0.1',
    description='',  # noqa
    long_description=read(BASE_DIR, 'README.rst'),
    author='Max Brauer',
    author_email='max@max-brauer.de',
    entry_points=entry_points,
    extras_require=extras_require,
    include_package_data=True,
    install_requires=requires,
    license='Other/Proprietary License',
    packages=find_packages(exclude=['tests*']),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
