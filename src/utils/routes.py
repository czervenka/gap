from webapp2_extras.routes import PathPrefixRoute
from webapp2 import Router
from utils.imports import import_class
from types import StringTypes
from collections import Iterable

def include(prefix, routes):
    if isinstance(routes, StringTypes):
        routes = import_class('%s.routes' % routes)
    elif hasattr(routes, 'routes'):
        routes = routes.routes

    routes = [ Router.route_class(*route) if isinstance(route, tuple) else route for route in routes ]

    return PathPrefixRoute(prefix, routes)
