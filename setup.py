""" 
Write code for project management configuration settings. 
"""

from setuptools import setup, find_packages

# Read the contents of requirements.txt for dependencies
with open("requirements.txt") as f:
    required = f.read().splitlines()
    
setup(
    name="hotel_reservation_project",
    version="0.1.0",
    author="Maxie",
    author_email="hoangminh261003@gmail.com",
    packages=find_packages(),
    install_requires=required,
)