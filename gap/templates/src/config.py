import os

ROOT_PATH = os.path.dirname(__file__)

# Template paths in the order in which they are resolved
TEMPLATES_PATH = (
    os.path.join(ROOT_PATH, 'templates'),
)

# needs to point to the same path / uri as in app.yaml
STATIC_PATH = os.path.join(ROOT_PATH, 'static')
STATIC_URL = '/static'

# default settings when not set in gap.conf.settings
DEFAULT_SETTINGS = {
    'DEBUG': True  # set to False on production server !!
}

