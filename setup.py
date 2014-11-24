"""
Explain
"""
from setuptools import setup, find_packages

setup(
    name="The Forge",
    version="0.1",
    packages=find_packages(),
    install_requires=["flask==0.10.1", "flask-sqlalchemy==2.0"],
    author='Alan Erwin',
    author_email='aerwin3@gmail.com',
    description='The forge is an interactive Dnd environment.'
)
