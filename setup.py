from setuptools import setup, find_packages

with open('README.md', 'r') as file :
     long_description=file.read()

setup(
name='pgbackup',
long_description=long_description,
packages=find_packages('src')
)
