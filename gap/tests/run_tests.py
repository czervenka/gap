#!/usr/bin/env python
'''
simple shortcut for running nosetests via python
replacement for *.bat or *.sh wrappers
'''
import sys
import os
from os.path import dirname, realpath, join
import logging
import nose
import re

from gap.utils.setup import fix_sys_path, setup_testbed

app_path = dirname(realpath(__file__))
fix_sys_path()
# TESTBED = setup_testbed()
os.chdir(dirname(__file__))
sys.path.insert(0, realpath(dirname(__file__)))

CONFIG = nose.config.Config(
    verbosity=2,
    loggingLevel=logging.WARNING,
    withGae=1,
    withoutSandbox=1,
    gaeApplication=app_path,
    where=realpath(dirname(__file__)),
    # nocapture='NOSE_NOCAPTURE',
    stop=1,
)

def run_all():
    logging.debug('Running tests with arguments: %r' % sys.argv)

    nose.run_exit(
        config = CONFIG
    )

class TestLoader(nose.loader.TestLoader):

    def __init__(self):
        super(self.__class__, self).__init__(config=CONFIG)

if __name__ == '__main__':
    run_all()
