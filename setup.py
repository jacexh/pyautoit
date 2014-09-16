#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from distutils.core import setup
from setuptools import setup
import autoit

setup(
    name='PyAutoIt',
    version=autoit.__version__,
    packages=['autoit'],
    packages_data={'': ['lib\\AutoItX3.dll', 'lib\\AutoItX3_x64.dll']},
    url='https://github.com/jacexh/pyautoit',
    include_package_data=True,
    license='MIT',
    author='Jace Xu',
    author_email='jace@xuh.me',
    description='Python Wrapper for AutoIt v3',
)
