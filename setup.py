#!/usr/bin/env python3
__title__ = 'yaglib'
__version__ = '0.1.01'
__license__ = 'Apache License, Version 2.0 and MIT License'


# import statements
import os
import sys
import distutils.extension
from distutils.util import get_platform
try:
    # First try to load most advanced setuptools setup.
    from setuptools import setup
except:
    # Fall back if setuptools is not installed.
    from distutils.core import setup

platform = get_platform()

# check Python's version
if sys.version_info < (3, 4):
    sys.stderr.write('This module requires at least Python 3.4\n')
    sys.exit(1)

# check linux platform
if not platform.startswith('linux'):
    sys.stderr.write("bluez is not available on %s\n" % platform)
    sys.exit(1)


classif = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: System :: Networking',
    'Topic :: Communications',    
    ]

setup(
    name=__title__,
    version=__version__,
    description='yaglib: yet another GATT library',
    author='Peter Michalek',
    author_email='peter@michalek.org',
    maintainer='Peter Michalek',
    maintainer_email='peter@michalek.org',
    packages=['yaglib'],
    package_data={'': ['LICENSE']},
    license="Apache 2.0 and MIT",
    long_description="Python Bluetooth LE (Low Energy) peripheral GATT Library",
    url='https://github.com/manylabs/yaglib',
    package_dir={'yaglib': 'yaglib'},
    zip_safe=False,
    include_package_data=True,
    platforms=["Linux"],
    classifiers=classif
)

