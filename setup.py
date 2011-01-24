#!/usr/bin/env python
from distutils.core import setup

setup(
    name='fabric-utils',
    version='0',
    description="",
    author="Tomasz Wysocki",
    author_email="tomasz@wysocki.info",
    install_requires=(
        'fabric',
    ),
    packages=[
        'fabric_utils',
    ],
)
