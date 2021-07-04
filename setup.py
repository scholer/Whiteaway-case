"""
Install using `pip install -e .`

This will make `src/` available as an importable package.

"""

from setuptools import find_packages, setup

setup(
    name='RS-Whiteaway-case',
    packages=find_packages(),
    version='0.1.0',
    description='Whiteaway case opgave Juni 2021.',
    author='Rasmus Scholer Sorensen',
    license='',
)
