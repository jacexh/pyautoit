#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import autoit
import os

setup(
    name='PyAutoIt',
    version=autoit.__version__,
    packages=['autoit'],
    package_data={'': ['lib\\*.dll']},
    url='https://github.com/jacexh/pyautoit',
    license='MIT',
    author='Jace Xu',
    author_email='jace@xuh.me',
    description='Python binding for AutoItX3.dll',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Win32 (MS Windows)",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing"
    ],
    long_description=open(
        os.path.join(os.path.dirname(__file__), "README.rst"), 'r').read())
