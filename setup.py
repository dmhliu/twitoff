#setup.py
from setuptools import setup

setup(
    name='twitoff',
    packages=['twitoff'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)