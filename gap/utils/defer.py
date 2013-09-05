__author = 'czervenka at github.com'
import json
import webapp2
from google.appengine.api import taskqueue
from gap.utils.imports import import_class


def defer(callback, *args, **kwargs):
    if '_queue_name' in kwargs:
        queue_name = kwargs['_queue_name']
        del kwargs['_queue_name']
    else:
        queue_name = 'utils-defer'
    callback = "%s.%s" % (callback.__module__, callback.__name__)
    taskqueue.add(
        url='/utils/defer/%s/%s' % (queue_name, callback,),
        params={'args': json.dumps(args), 'kwargs': json.dumps(kwargs)},
        queue_name=queue_name,
    )


class _Defer(webapp2.RequestHandler):

    def post(self, queue_name, callback):
        request = self.request
        callback = import_class(callback)
        callback(*json.loads(request.get('args')), **json.loads(request.get('kwargs')))


app = webapp2.WSGIApplication([
    ('/utils/defer/(.*)/(.*)', _Defer),
])
