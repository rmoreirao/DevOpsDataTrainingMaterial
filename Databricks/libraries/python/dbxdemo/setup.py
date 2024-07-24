# To enable the build agent to use Python Setuptools to package the Python wheel to give to the release pipeline,

# setup.py
from setuptools import setup, find_packages

setup(
  name = 'dbxdemo',
  version = '0.1.0',
  packages = ['.']
)