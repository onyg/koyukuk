#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import distribute_setup
    distribute_setup.use_setuptools()
except:
    pass

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import os
import re


with open(os.path.join(os.path.dirname(__file__), 'koyukuk', '__init__.py')) as f:
    version = re.search("__version__ = '([^']+)'", f.read()).group(1)

with open('requirements/base.txt', 'r') as f:
    requires = [x.strip() for x in f if x.strip()]

with open('requirements/test.txt', 'r') as f:
    test_requires = [x.strip() for x in f if x.strip()]

with open('README.rst', 'r') as f:
    readme = f.read()


CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

basic_setup = dict(
    name='koyukuk',
    author='sinnedh, onyg',
    version=version,
    description="koyukuk metrics",
    long_description=readme,
    url='https://github.com/onyg/koyukuk',
    license='MIT License',
    packages=find_packages(exclude=['tests', 'tests.*']),
    test_suite='tests',
    tests_require=test_requires,
    install_requires=requires,
    extras_require={'test': test_requires},
    classifiers=CLASSIFIERS,
    platforms=['any'],
    entry_points={
        'console_scripts': [
            'koyukukf = koyukuk.commands.main:main',
        ],
    },
)

setup(**basic_setup)
