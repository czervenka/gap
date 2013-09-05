#!/usr/bin/env python

'''
simple shortcut for running nosetests via python
replacement for *.bat or *.sh wrappers
'''

import sys
import logging
from os.path import abspath, dirname, join
import nose

sys.path.insert(0, join(abspath(dirname(__file__)), '..'))

import src

# Enable included lib files.
sys.path.insert(0, join(abspath(dirname(src.__file__)), 'lib'))


def run_all(argv=None):
    sys.exitfunc = lambda msg = 'Process shutting down...': sys.stderr.write(msg + '\n')

    argv  = (set(argv) | {
        '--where=%s' % dirname(abspath(src.__file__)),
        '-c nose.cfg',
        '--with-gae',
        '--gae-application=%s' % dirname(abspath(src.__file__)),
        '--verbose',
        '--without-sandbox'
    }) - {'./run_tests.py'}

    logging.debug('Running tests with arguments: %r' % argv)

    nose.run_exit(
        argv=list(argv),
        defaultTest=abspath(dirname(__file__)),
    )

if __name__ == '__main__':
    run_all(sys.argv)
