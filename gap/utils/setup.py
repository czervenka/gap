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
import sys
from os.path import join, abspath, realpath, dirname
from distutils.spawn import find_executable

GAE_APP_ROOT = 'src'
GAE_RUNTIME_ROOT = None

_PATH_FIXED = 0

def find_gae_runtime_path():
    return dirname(realpath(find_executable('appcfg.py')))

def fix_sys_path(app_src=None):
    global _PATH_FIXED
    if not _PATH_FIXED:
        gae_path = find_gae_runtime_path()
        sys.path.insert(0, gae_path)
        # sys.path.insert(0, join(gae_path, 'lib'))
        import dev_appserver
        dev_appserver.fix_sys_path()
        _PATH_FIXED = 1

    if app_src and _PATH_FIXED < 2:
        sys.path.insert(0, app_src)
        _PATH_FIXED = 2

def read_yaml(app_src):
    import yaml
    return yaml.load(open(join(app_src, 'app.yaml'), 'r').read())

def setup_stubs(app_src):

    from google.appengine.api import apiproxy_stub_map

    apiproxy_stub_map.apiproxy = apiproxy_stub_map.APIProxyStubMap()

    from google.appengine.api import urlfetch_stub
    apiproxy_stub_map.apiproxy.RegisterStub(
        'urlfetch',
        urlfetch_stub.URLFetchServiceStub()
    )
    from google.appengine.api.memcache import memcache_stub
    apiproxy_stub_map.apiproxy.RegisterStub(
        'memcache',
        memcache_stub.MemcacheServiceStub(),
    )
    from google.appengine.api import datastore_file_stub
    apiproxy_stub_map.apiproxy.RegisterStub(
            'datastore',
            datastore_file_stub.DatastoreFileStub(app_id=read_yaml(app_src)['application'], datastore_file=join(dirname(app_src), '.tmp', 'test1.db'))
    )
    import app

DEFAULT_TESTBEDS = (
    'datastore',
    'app_identity',
    'memcache',
    'files',
    'urlfetch',
    'mail',
    'search',
)
def setup_testbed(stubs=DEFAULT_TESTBEDS, env={}):
    from google.appengine.ext import testbed
    t = testbed.Testbed()
    if env:
        t.setup_env(**env)
    t.activate()
    for stub in stubs:
        if stub == 'datastore':
            stub = 'datastore_v3'
        getattr(t, 'init_%s_stub' % stub)()
        if stub == 'urlfetch':
            t.urlfetch_stub = t.get_stub('urlfetch')
        elif stub == 'mail':
            t.mail_stub = t.get_stub(testbed.MAIL_SERVICE_NAME)
    import app
    return t
