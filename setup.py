from setuptools import setup, find_packages
from delivery import __version__
import os


def read_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

try:
    with open("requirements/prod", "r") as f:
        install_requires = [x.strip() for x in f.readlines()]
except IOError:
    install_requires = []

setup(
    name='delivery',
    version=__version__,
    description="Micro-service for running deliveries on Uppmax",
    long_description=read_file('README.md'),
    keywords='bioinformatics',
    author='SNP&SEQ Technology Platform, Uppsala University',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': ['delivery-ws = delivery.app:start']
    },
)
