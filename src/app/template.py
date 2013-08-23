import config
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(config.TEMPLATES_PATH),
    autoescape=True,
)

JINJA_ENVIRONMENT.globals['STATIC_URL'] = config.STATIC_URL


def get_template(template_path):
    return JINJA_ENVIRONMENT.get_template(template_path)
