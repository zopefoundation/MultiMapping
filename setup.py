##############################################################################
#
# Copyright (c) 2010 Zope Corporation and Contributors.
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

setup(name='MultiMapping',
      version = '2.13.1.dev0',
      url='http://pypi.python.org/pypi/MultiMapping',
      license='ZPL 2.1',
      description="Special MultiMapping objects used in Zope2.",
      author='Zope Corporation and Contributors',
      author_email='zope-dev@zope.org',
      long_description=open('README.txt').read() + '\n' +
                       open('CHANGES.txt').read(),

      packages=find_packages('src'),
      package_dir={'': 'src'},
      ext_modules=[Extension(
            name='MultiMapping._MultiMapping',
            include_dirs=['include', 'src'],
            sources=[join('src', 'MultiMapping', '_MultiMapping.c')],
            depends=[join('include', 'ExtensionClass', 'ExtensionClass.h')]),
      ],
      install_requires=['ExtensionClass<4.0dev'],
      include_package_data=True,
      zip_safe=False,
      )
