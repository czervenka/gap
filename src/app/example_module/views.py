from utils.decorators import as_view

@as_view
def module_welcome_screen(request, response):
    return 'Welcome to example module'

