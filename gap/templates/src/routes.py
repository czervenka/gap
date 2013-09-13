import webapp2
import config
from gap.routes import include


routes = (
    ('/', 'gap.views.welcome_screen'),
    # include('/my_module', 'my_module.routes'),

    # any other url is redirected to "404 Not Found"
    ('/.*', 'gap.views.not_found'),  # all other requests end up with '404 Not Found' error
)




