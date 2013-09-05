#!/usr/bin/env python
from os.path import dirname, realpath, join
import IPython
from gap.utils.setup import fix_sys_path, build_stubs

app_path = join(realpath(dirname(__file__)), 'src')
fix_sys_path(app_src)
build_stubs()

IPython.embed()
