import os


ROOT_PATH = os.path.dirname(__file__)


DEBUG = True

TEMPLATES_PATH = os.path.join(ROOT_PATH, 'templates')
STATIC_PATH = os.path.join(ROOT_PATH, 'static')  # needs to point to the same path as in app.yaml
STATIC_URL = '/static'  # needs to point to the same url as in app.yaml
