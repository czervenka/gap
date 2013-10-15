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

__author__ = 'Robin Gottfried <google@kebet.cz>'

"""
Simple pip wraper to work with virtual environment and google app engine.

Use it the same way as pip. Each time gip is called, it updates symlinks to you application src/lib.

While creating / removing symlinks, gip does not touch any regular files / directories in src/lib

TODO: Rewrite :-) ... better to use setuptools or some other library to get distributions and top-level packages/modules
"""

from sys import exit, argv
from os.path import join, basename, dirname, exists, islink, isdir
from os import symlink, environ, listdir, unlink
from time import sleep
from importlib import import_module
import pip

if not 'VIRTUAL_ENV' in environ:
    print 'Gae pip can work only in virtua environment'
    exit(1)

IGNORED_DISTS = set([
    'setuptools',
    'setuptools-dummy',
    'distribute',
    'ipython',
    'argparse',
    'pip',
    'rvirtualenv',
    'nose',
    'nosegae',
    'coverage',
    'rednose',
    'python-termstyle',
    'waitress',
    'webob',
    'webtest',
    'pycrypto',
    'mock',
])

LIB_PATH = join(dirname(dirname(__file__)), 'src', 'lib')

def error(*args):
    print '! ' + ' '.join(args)

VERBOSE = 0
def info(*args):
    if VERBOSE > 0:
        print ' '.join(args)

def unsymlink_module(path, lib_path):
    filename = basename(path)
    link_path = join(lib_path, filename)
    if islink(link_path):
        info('Unlinking obsolete ->%s' % link_path)
        unlink(link_path)
    elif not exists(link_path):
        error('Path %s not found' % link_path)


def symlink_module(path, lib_path):
    link_info = [path, join(lib_path, basename(path))]
    if not islink(link_info[1]):
        if not exists(link_info[0]):
            error('Error creating link %s' % link_info[0])
            return
        if exists(link_info[1]):
            print "Error creating link %r, there is another file with the same name." % link_info[1]
        print '%s -> %s' % tuple(link_info)
        symlink(*link_info)

def list_distributions():
    import pkg_resources
    env = pkg_resources.Environment()
    for dist_name in env:
        yield dist_name

def list_distribution_paths(dist_name):
    import pkg_resources
    if dist_name in IGNORED_DISTS:
        info('* Exclude %r' % dist_name)
        return []
    distribution = pkg_resources.get_distribution(dist_name)
    if not str(distribution.location).strip():
        info('* Exclude %r (empty location)' % dist_name)
        return []
    path = join(distribution.location, distribution.egg_name() + '.egg-info')
    if not exists(path):
        path = join(distribution.location, distribution.egg_name().replace('-', '_') + '.egg-info')
    if not exists(path):
        path = join(distribution.location, dist_name + '.egg-info')
    if not exists(path):
        path = join(distribution.location, dist_name.replace('-', '_') + '.egg-info')
    if exists(path):
        if isdir(path):
            p = join(path, 'top_level.txt')
            if exists(p):
                path = p
            else:
                info('- Exclude %r (not top_level.txt)' % dist_name)
                return []
        else:
            info('- Exclude %r (unsupported egg format)' % dist_name)
            return []
    if not exists(path):
        path = join(distribution.location, 'EGG-INFO', 'top_level.txt')

    if path.startswith(environ['VIRTUAL_ENV']):
        info('- Include %r' % dist_name)
        info('     path: %r / location: %r, name: %r, egg: %r' % (path, distribution.location, dist_name, distribution.egg_name()))
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
                    elif path.endswith('.pyc') and exists(path[:-1]):
                        path = path[:-1]
                except ImportError:
                    error('Error finding module %r' % package)
                    continue
            paths.append(path)
    else:
        info('* Exclude %r (not in venv)' % dist_name)
        return []
    return paths

def update_symlinks(lib_path):

    info('\n\nUpdating symlinks ...')

    linked_libs = ([ lib for lib in listdir(lib_path) ])
    # print 'Linked libs: %s' % linked_libs

    installed_libs = {}
    for dist in list_distributions():
        for path in list_distribution_paths(dist):
            filename = basename(path)
            installed_libs[filename] = path
    info('Installed libs: %s' % installed_libs)

    for lib in linked_libs:
        if not lib in installed_libs:
            unsymlink_module(lib, lib_path)

    for lib, path in installed_libs.items():
        if not lib in linked_libs:
            symlink_module(path, lib_path)

    info('done')


def run(lib_path):
    global VERBOSE
    pip_exception = None

    if len(argv) >= 2 and argv[1].rsplit('.', 1)[-1] == 'gip':
        pip_args = ['install']
        pip_args += argv[2:]
        pip_args.extend(['-r', argv[1]])
    else:
        pip_args = argv[1:]

    if '-v' in argv or '--verbose' in argv:
        VERBOSE = 1

    info('Arguments passed to pip: %r' % pip_args)
    try:
        pip.main(pip_args)
    except (Exception, SystemExit), pip_exception:
        pass

    if len(argv) > 1 and argv[1] in ('install' , 'uninstall'):
        sleep(0.5)  # give the package time to finish
        update_symlinks(lib_path)

    if pip_exception:
        raise pip_exception

if __name__ == '__main__':
    run(LIB_PATH)
