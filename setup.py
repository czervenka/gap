#!/usr/bin/env python
import os
from setuptools import setup, findall, find_packages
from collections import defaultdict

def collect_files(path, prefix=''):
    ret = defaultdict(list)
    files = findall(path)
    for f in files:
        ret[os.path.join(prefix,os.path.dirname(f))].append(f)
    return ret.items()


setup(
    name='gap',
    version='0.2',
    description='Google App Engine project bootstrap',
    author='Robin Gottfried',
    author_email='google@kebet.cz',
    url='https://github.com/czervenka/gap',
    packages=['gap', 'gap.utils'],
    scripts=['gap/bin/gap'],
    # data_files=collect_files('templates', 'gap'),
    include_package_data=True,
    requires=[],
)
