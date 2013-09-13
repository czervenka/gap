#!/usr/bin/env python2
# Copyright 2007 Robin Gottfried <copyright@kebet.cz>
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

__author__ = 'Robin Gottfried <google@kebet.cz>'

"""
Simple pip wraper to work with virtual environment and google app engine.

Use it the same way as pip. Each time gip is called, it updates symlinks to you application src/lib.

While creating / removing symlinks, gip does not touch any regular files / directories in src/lib
"""

from sys import exit, argv
from os.path import join, basename, dirname, exists, islink
from os import symlink, environ, listdir, unlink
from importlib import import_module
import pip

if not 'VIRTUAL_ENV' in environ:
    print 'Gae pip can work only in virtua environment'
    sys.exit(1)

IGNORED_DISTS = set(['setuptools', 'ipython', 'argparse', 'pip', 'rvirtualenv'])

LIB_PATH = join(dirname(dirname(__file__)), 'src', 'lib')


def unsymlink_module(path, lib_path):
    filename = basename(path)
    link_path = join(lib_path, filename)
    if islink(link_path):
        print 'Unlinking obsolete ->%s' % link_path
        unlink(link_path)
    elif not exists(link_path):
        print 'Path %s not found' % link_path


def symlink_module(path, lib_path):
    link_info = (path, join(lib_path, basename(path)))
    if not islink(link_info[1]):
        if not exists(link_info[0]):
            print 'Error creating link %s' % link_info[0]
            return
        if exists(link_info[1]):
            print "Error creating link %r, there is another file with the same name." % link_info[1]
        print '%s -> %s' % link_info
        symlink(*link_info)

def list_distributions():
    import pkg_resources
    env = pkg_resources.Environment()
    for dist_name in env:
        yield dist_name

def list_distribution_paths(dist_name):
    import pkg_resources
    if dist_name in IGNORED_DISTS:
        return []
    distribution = pkg_resources.get_distribution(dist_name)
    path = join(distribution.location, distribution.egg_name() + '.egg-info', 'top_level.txt')
    if not exists(path):
        path = join(distribution.location, dist_name + '.egg-info', 'top_level.txt')
    if path.startswith(environ['VIRTUAL_ENV']):
        paths = []
        for package in [ line.strip() for line in open(path).readlines() ]:
            if not package:
                continue
            path = join(distribution.location, package)
            if not exists(path):
                try:
                    package = import_module(package)
                    path = package.__file__
                    if basename(path).startswith('__init__.'):
                        path = dirname(path)
                except ImportError:
                    print 'Error finding module %r' % package
                    continue
            paths.append(path)
    else:
        return []
    return paths

def update_symlinks(lib_path):

    print '\n\nUpdating symlinks ...'

    linked_libs = ([ lib for lib in listdir(lib_path) ])
    # print 'Linked libs: %s' % linked_libs

    installed_libs = {}
    for dist in list_distributions():
        for path in list_distribution_paths(dist):
            filename = basename(path)
            installed_libs[filename] = path
    # print 'Installed libs: %s' % installed_libs

    for lib in linked_libs:
        if not lib in installed_libs:
            unsymlink_module(lib, lib_path)

    for lib, path in installed_libs.items():
        if not lib in linked_libs:
            symlink_module(path, lib_path)

    print 'done'


def run(lib_path):
    pip_exception = None

    if len(argv) >= 2 and argv[1].rsplit('.', 1)[-1] == 'gip':
        pip_args = ['install']
        pip_args += argv[2:]
        pip_args.extend(['-r', argv[1]])
    else:
        pip_args = argv[1:]

    print repr(pip_args)
    try:
        pip.main(pip_args)
    except (Exception, SystemExit), pip_exception:
        pass

    if len(argv) > 1 and argv[1] in ('install' , 'uninstall'):
        update_symlinks(lib_path)

    if pip_exception:
        raise pip_exception

if __name__ == '__main__':
    run(LIB_PATH)
