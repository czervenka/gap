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

__all__ = ['prepare_environment']

import sys
from os.path import dirname, join

def prepare_environment():
    sys.path.insert(0, join(dirname(dirname(__file__)), 'lib'))

prepare_environment()



import webapp2
from google.appengine.ext.webapp import util
import config
from routes import routes

handler = webapp2.WSGIApplication(routes=routes, debug=config.DEBUG)
