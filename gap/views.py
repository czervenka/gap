from utils.decorators import as_view
from gap.template import get_template
from StringIO import StringIO


@as_view
def welcome_screen(handler):
    return get_template("homepage.html").render({
        'project_name': 'Example project',
    })


@as_view
def not_found(handler, *args, **kwargs):
    handler.response.set_status(404)
    text = 'The page you are requesting was not found on this server.'

    from gap.conf import settings
    if settings['DEBUG']:
        buffer = StringIO()
        dump_routes(buffer)
        buffer.seek(0)
        return text + '<br>The known rotes are...<br><pre>' + buffer.read() + '</pre>'
    else:
        return text

def dump_routes(response, routes=None, indent=''):
    if routes is None:
        from routes import routes
    for route in routes:
        dump_route(response, route, indent)

def dump_route(response, route, indent=''):
    if isinstance(route, (tuple, list)):
        response.write(route[0] + ' -> ' + route[1] + '\n')
    elif hasattr(route, 'routes'):
        response.write(indent + route.prefix + ':' + '\n')
        dump_routes(response, route.routes, indent+'  ')
    elif hasattr(route, 'regex'):
        response.write(indent + route.regex.pattern + ' -> ' + repr(route.handler) + '\n')
    else:
        raise TypeError('Unknown route class %s' % route.__class__.__name__)
