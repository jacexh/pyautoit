# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import re
import os


with open("autoit/__init__.py", 'r') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        f.read(), re.MULTILINE).group(1)

setup(
    name='PyAutoIt',
    version=version,
    packages=['autoit'],
    package_data={'': ['lib\\*.dll']},
    url='https://github.com/jacexh/pyautoit',
    license='MIT',
    author='Jace Xu',
    author_email='jace.xh@gmail.com',
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
