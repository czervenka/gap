# -*- coding: utf-8 -*-
# Copyright 2007 Robin Gottfried <google@kebet.cz> and Lukas Lukovsky
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
# @author Lukas Lukovsky
#
# part of gap project (https://github.com/czervenka/gap)
__author__ = 'Lukas Lukovsky'

import json
from unittest import TestCase
from gap.utils.setup import setup_testbed


class TestBase(TestCase):

    # Allow to share the setUpClass method among all parallel test classes
    _multiprocess_shared_ = True

    # Allow concurrent run of fixtures
    _multiprocess_can_split_ = True

    @classmethod
    def setUpClass(cls):
        # Begin with testbed instance
        cls.testbed = setup_testbed()

    @classmethod
    def tearDownClass(cls):
        cls.testbed.deactivate()


class TestJsonApiBase(TestBase):

    JSON_HEADERS = {'content-type': 'application/json; encoding=utf-8'}

    def get_json_response(self, url, method, code=200, payload=None, headers=JSON_HEADERS):
        from google.appengine.api.urlfetch import fetch
        result = fetch(url, method, payload, headers=headers)
        self.assertEqual(result.status_code, code)
        return json.loads(result.content)
