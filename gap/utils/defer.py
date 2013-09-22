#!/usr/bin/env python2
# Copyright 2007 Robin Gottfried <google@kebet.cz>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# @author Robin Gottfried <google@kebet.cz>
# part of gap project (https://github.com/czervenka/gap)
__author = 'google@kebet.cz'

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
