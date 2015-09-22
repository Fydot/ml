#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import find_packages, setup

from ml import __version__

setup(
    name='ml',
    version=__version__,
    license='PRIVATE',
    author='',
    author_email='',
    description='robin know everything',
    url='git@github.com:Fydot/ml.git',
    packages=find_packages(exclude=['tests']),
    package_data={'ml': ['CHANGES.rst', 'README.md']},
    zip_safe=False,
    install_requires=[
        'numpy',
        'scikit-learn',
    ],
    entry_points={
        'console_scripts': [],
    }

)
