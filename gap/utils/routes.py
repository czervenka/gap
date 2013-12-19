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


class BaseRouter(webapp2.Router):

    def _get_filters(self):
        import config
        return [import_class(f) for f in getattr(config, 'REQUEST_FILTERS', [])]  # copy

    def _run_filters(self, direction, method, *args):
        to_return = False
        filters = self._get_filters()[::direction]
        for filter_ in filters:
            if hasattr(filter_, method):
                if not getattr(filter_, method)(*args):
                    to_return = False
                    break
                else:
                    to_return = True
        return to_return

    def _dispatch(self, request, response):
        self._run_filters(1, 'process_request', request, response)
        to_return = super(BaseRouter, self).dispatch(request, response)
        if to_return is not None:  # compatibility with webap2 router
            response = to_return
        self._run_filters(-1, 'process_response', request, response)
        return response

    def dispatch(self, request, response):
        try:
            response = self._dispatch(request, response)
        except Exception, exception:
            result = self._run_filters(1, 'process_exception', request, response, exception)
            if not result:
                raise
        return response

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


