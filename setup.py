# author:	Andre Alves
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


# Get the long description from the README file
with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='ipcamera',
    version='0.1.0',
    description='IpCamera enables you to access your smartphone camera remotely in python.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/1cybersheep1/ipcamera',
    author='Andre Alves',
    author_email='andre.alves.pypi@gmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='ipcamera remote camera android',
    packages=find_packages(),
    setup_requires=['setuptools>=38.6.0'],
    install_requires=['opencv', 'numpy']
)