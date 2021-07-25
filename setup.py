#!/usr/bin/env python
from setuptools import setup, find_packages


install_requires = [
    "boto3>=1.9.201",
    "botocore>=1.12.201"
]


setup(
    name="pipresolverbug",
    version="0.1",
    install_requires=install_requires
)
