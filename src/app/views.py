from utils.decorators import as_view


@as_view
def welcome_screen(request, response):
    return "It works!"

@as_view
def not_found(request, response, *args, **kwargs):
    response.set_status(404)
    return 'The page you are requesting was not found on this server.'
