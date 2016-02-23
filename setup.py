# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except IOError:
    long_description = open("README.md").read()

setup(
    name="wegene",
    version="0.0.4",
    url="https://github.com/xraywu/wegene-python-sdk",
    description="WeGene SDK for Python",
    license="MIT",
    author="Eddie Wu",
    author_email="xrayxiaoli@gmail.com",
    package_dir={ 'wegene': 'wegene' },
    packages=find_packages(),
    install_requires=[
        "Unirest==1.1.6",
        "jsonpickle==0.7.1",
        "poster==0.8.1",
    ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
