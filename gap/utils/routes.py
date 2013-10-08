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

from types import StringTypes

import webapp2
from webapp2_extras.routes import PathPrefixRoute
from webapp2 import Router
from gap.utils.imports import import_class


def include(prefix, routes):
    if isinstance(routes, StringTypes):
        routes = import_class('%s.routes' % routes)
    elif hasattr(routes, 'routes'):
        routes = routes.routes

    routes = [ Router.route_class(*route) if isinstance(route, tuple) else route for route in routes ]

    return PathPrefixRoute(prefix, routes)


class RouteEx(webapp2.Route):
    '''
    Adds strict_slash parameter which allows to control wheter urls with and
    without slash will lead to the same handler.
    '''

    def __init__(self, *args, **kwargs):
        self._strict_slash = kwargs.pop('strict_slash', False)
        super(RouteEx, self).__init__(*args, **kwargs)
        if not self._strict_slash:
            self.template += '<__slash:/?>'

    def match(self, request):
        res = super(RouteEx, self).match(request)
        if res and not self._strict_slash:
            self, args, kwargs = res
            kwargs.pop('__slash')
            res = (self, args, kwargs)
        return res


