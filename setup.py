#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import autoit

setup(
    name='PyAutoIt',
    version=autoit.__version__,
    packages=['autoit'],
    package_data={'': ['lib\\*.dll']},
    url='https://github.com/jacexh/pyautoit',
    license='MIT',
    author='Jace Xu',
    author_email='jace@xuh.me',
    description='Python Wrapper for AutoIt v3',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Win32 (MS Windows)",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing"
    ]
)
