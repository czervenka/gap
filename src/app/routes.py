import webapp2
import config
from utils.routes import include


routes = (
    ('/', 'app.views.welcome_screen'),
    include('/example_module', 'app.example_module.routes'),

    # any other url is redirected to "404 Not Found"
    ('/.*', 'app.views.not_found'),  # all other requests end up with '404 Not Found' error
)




