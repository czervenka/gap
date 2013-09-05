# -*- coding: utf-8 -*-

import requests
import json
from test_base import TestBase


class TestJsonApiBase(TestBase):
    POST = 'post'
    GET = 'get'
    DELETE = 'delete'

    JSON_HEADER = {'content-type': 'application/json'}

    def get_json_response(self, url, type, code=200, data=None, headers=None, params=None):
        method = getattr(requests, type)
        r = method(url, data=data, headers=headers, params=params)
        self.assertEqual(r.status_code, code)
        return json.loads(r.text)
