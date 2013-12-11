from gap.utils.decorators import as_view

@as_view
def module_welcome_screen(handler):
    # handler is an instance of webapp2.RequestHandler
    # for request, access handler.request
    # for response, access handler.response
    # it's possible to access RquestHandler's methods like:
    # handler.redirect(url)
    return 'Welcome to example module'

