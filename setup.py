#!/usr/bin/env python
# Copyright 2007 Robin Gottfried <google@kebet.cz>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# @author Robin Gottfried <google@kebet.cz>
# part of gap project (https://github.com/czervenka/gap)
__version__ = '0.4.6'

import os
from os.path import join, dirname
from setuptools import setup, findall
from collections import defaultdict


try:
    import multiprocessing
except ImportError:
    pass


def collect_files(path, prefix=''):
    ret = defaultdict(list)
    files = findall(path)
    for f in files:
        ret[os.path.join(prefix,os.path.dirname(f))].append(f)
    return ret.items()

long_description=open(join(dirname(__file__), 'README.rst')).read()
long_description += '\n\nChanges\n=======\n' + open(join(dirname(__file__), 'changes.rst')).read()

setup(
    name='gap',
    version=__version__,
    description='Google App Engine project bootstrap',
    long_description=long_description,
    author='Robin Gottfried',
    author_email='google@kebet.cz',
    url='https://github.com/czervenka/gap',
    packages=['gap', 'gap.utils'],
    scripts=['gap/bin/gap'],
    zip_safe = False,
    license='Apache License 2.0',
    requires=['pip', 'ipython', ],
    include_package_data=True,
    test_loader='gap.tests.run_tests:TestLoader',
    test_suite='gap.tests',
    tests_require=[
        'nose',
        'nosegae',
        'mock',
    ],
)
