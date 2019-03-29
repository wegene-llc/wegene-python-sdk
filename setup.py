# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


long_description = 'WeGene Python SDK. For details check https://api.wegene.com'

setup(
    name="wegene",
    version="0.1.0",
    url="https://github.com/xraywu/wegene-python-sdk",
    description="WeGene SDK for Python",
    license="MIT",
    author="Eddie Wu",
    author_email="xrayxiaoli@gmail.com",
    package_dir={ 'wegene': 'wegene' },
    packages=find_packages(),
    install_requires=[
        "requests==2.21.0",
        "jsonpickle==0.7.1",
    ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
    ]
)
