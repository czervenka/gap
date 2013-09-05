import webapp2

def as_view(func, methods=['get', 'post']):


    def _handle(self, *args, **kwargs):
        response = func(self.request, self.response, *args, **kwargs)
        if response is not None:
            self.response.write(response)

    class _View(webapp2.RequestHandler):

        for method in methods:
            locals()[method] = _handle

    return _View
