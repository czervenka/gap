#!/usr/bin/env python
import sys
from os.path import dirname, realpath, join
import IPython
from gap.utils.setup import fix_sys_path, setup_testbed, setup_stubs

app_path = join(realpath(dirname(dirname(__file__))), 'src')
fix_sys_path(app_path)
TESTBED = setup_testbed()

# preimport common google apis
from google.appengine.api.urlfetch import fetch
from google.appengine.ext import db, ndb
from google.appengine.api import memcache

IPython.embed()
