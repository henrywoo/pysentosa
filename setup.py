#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import codecs
import os

def read(fname):
    """ Read long description given a file name
    PyPI supports .rst but not .md. rst file will be displayed in PyPI in HTML format。
    """
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

LONG_DESCRIPTION = read("README.rst")

setup(
    name = "pysentosa",
    version="0.1.27",
    packages = find_packages(),
    package_dir ={'pysentosa': 'pysentosa'},
    package_data={'pysentosa': ['sentosa_.so']},
    description = "pysentosa - Python API for sentosa trading system",
    long_description = LONG_DESCRIPTION,
    author = "Wu Fuheng",
    author_email = "henry.woo@outlook.com",

    license = "GPL",
    keywords = ("sentosa", "python"),
    platforms = "Independant",
    url = "http://www.quant365.com",
    #zip_safe=True,
)
