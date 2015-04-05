##############################################################################
#
# Copyright (c) 2010 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

from os.path import join
from setuptools import setup, find_packages, Extension
import os
import platform
import sys

# PyPy won't build the extension.
py_impl = getattr(platform, 'python_implementation', lambda: None)
is_pypy = py_impl() == 'PyPy'
is_pure = 'PURE_PYTHON' in os.environ
py3k = sys.version_info >= (3, )
if is_pypy or is_pure or py3k:
    ext_modules = []
else:
    ext_modules = [
        Extension(
            name='MultiMapping._MultiMapping',
            include_dirs=['include', 'src'],
            sources=[join('src', 'MultiMapping', '_MultiMapping.c')],
        ),
    ]


setup(
    name='MultiMapping',
    version='3.0.dev0',
    url='http://pypi.python.org/pypi/MultiMapping',
    license='ZPL 2.1',
    description="Special MultiMapping objects used in Zope2.",
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    long_description=open('README.txt').read() + '\n' + open('CHANGES.txt').read(),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    ext_modules=ext_modules,
    install_requires=['ExtensionClass'],
    include_package_data=True,
    zip_safe=False,
    )
