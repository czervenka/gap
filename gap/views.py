from utils.decorators import as_view
from gap.template import get_template


@as_view
def welcome_screen(request, response):
    return get_template("homepage.html").render({
        'project_name': 'Example project',
    })

@as_view
def not_found(request, response, *args, **kwargs):
    response.set_status(404)
    return 'The page you are requesting was not found on this server.'
