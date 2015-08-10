#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import codecs, os

def read(fname):
    """
    定义一个read方法，用来读取目录下的长描述
    我们一般是将README文件中的内容读取出来作为长描述，这个会在PyPI中你这个包的页面上展现出来，
    你也可以不用这个方法，自己手动写内容即可，
    PyPI上支持.rst格式的文件。暂不支持.md格式的文件，<BR>.rst文件PyPI会自动把它转为HTML形式显示在你包的信息页面上。
    """
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

LONG_DESCRIPTION = read("README.rst")

setup(
    name = "pysentosa",
    version="0.1.18",
    packages = find_packages(),
    data_files=[
      ('pysentosa', ['pysentosa/sentosa_.so']),
    ],
    description = "Pysentosa - Python API for sentosa trading system",
    long_description = LONG_DESCRIPTION,
    author = "Wu Fuheng",
    author_email = "henry.woo@outlook.com",

    license = "GPL",
    keywords = ("sentosa", "python"),
    platforms = "Independant",
    url = "http://www.quant365.com",
    #zip_safe=True,
)
