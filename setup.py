#! /usr/bin/python3
# coding: utf-8
# mail:zhuowangy2k@outlook.com
# a simple io package for ctf use python3

from setuptools import setup

setup(
    name='ioctf',
    version='0.1.1',
    author='Zhuo Wang',
    author_email='zhuowangy2k@outlook.com',
    url="https://github.com/WangZhuo2000/ioctf",
    description= 'a simple io package for ctf use python3',
    long_description='The website is [here](https://github.com/WangZhuo2000/ioctf)',
    long_description_content_type='text/markdown',
    packages=['ioctf'],
    install_requires=[]
)

# twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
# python3 setup.py sdist bdist_wheel