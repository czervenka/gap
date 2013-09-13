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
        sys.path.insert(0, join(gae_path, 'lib'))
        import dev_appserver
        dev_appserver.fix_sys_path()
        _PATH_FIXED = 1

    if app_src and _PATH_FIXED < 2:
        sys.path.insert(0, app_src)
        import app
        _PATH_FIXED = 2


def build_stubs():
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
