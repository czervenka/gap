import logging
import json
from gap.conf import settings
from datetime import datetime, date
import time


class JsonException(Exception):

    def __init__(self, code, message=None, exception=None):
        self.code = int(code)
        if message is None:
            message = self.get_status_message(code)
        self.message = message
        self.exception = exception

    def get_status_message(self, code):
        from httplib import responses
        return responses.get(self.code, 'Unknown status')


class MessageEncoder(json.JSONEncoder):

    def default(self, o):
        if hasattr(o, 'as_dict'):
            return o.as_dict()
        elif hasattr(o, 'to_dict'):
            return o.to_dict()
        elif isinstance(o, (date, datetime)):
            return time.mktime(o.timetuple())
        else:
            super(MessageEncoder, self).default(o)


class dumps(object):

    def __init__(self, data, **kwargs):
        self._data = data
        self.kwargs = kwargs

    def __str__(self):
        return self._dumps()

    def __unicode__(self):
        return unicode(self._dumps())

    def _dumps(self):
        return json.dumps(self._data, cls=MessageEncoder, **self.kwargs)


def json_response(fn):
    """
    The function result will be converted to JSON a send to response
    """

    def args_wrap(self, *args, **kwargs):
        exception = None
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        try:
            data = fn(self, *args, **kwargs)

            if data is not None:
                self.response.write(dumps(data, indent=4))
        except JsonException, exception:
            self.response.clear()
            self.response.status = exception.code
            data = {
                'error': {
                    'code': exception.code,
                    'message': exception.message,
                },
            }
        except Exception, exception:
            logging.exception(exception)
            self.response.clear()
            self.response.status = 500
            data = {
                'error': {
                    'code': 500,
                    'message': 'Internal Server Error',
                },
            }

        if exception:
            if settings['DEBUG']:
                from traceback import format_exc
                data['error']['traceback'] = format_exc()
            self.response.write(dumps(data))
    args_wrap.__name__ = fn.__name__
    return args_wrap
