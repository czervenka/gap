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
__version__ = '0.4'

import os
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


setup(
    name='gap',
    version=__version__,
    description='Google App Engine project bootstrap',
    author='Robin Gottfried',
    author_email='google@kebet.cz',
    url='https://github.com/czervenka/gap',
    packages=['gap', 'gap.utils'],
    scripts=['gap/bin/gap'],
    zip_safe = False,
    include_package_data=True,
    requires=[],
    test_loader='gap.tests.run_tests:TestLoader',
    test_suite='gap.tests',
    tests_require=[
        'nose',
        'nosegae',
        'mock',
    ],
)
