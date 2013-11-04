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
from gap.utils import setup

DEFAULT = object()

class TestBase(TestCase):

    testbed = None

    _gae_stubs = setup.DEFAULT_TESTBEDS

    # Allow to share the setUpClass method among all parallel test classes
    _multiprocess_shared_ = True

    # Allow concurrent run of fixtures
    _multiprocess_can_split_ = True

    @classmethod
    def setUpClass(cls):
        # Begin with testbed instance
        cls.testbed = setup.setup_testbed(stubs=cls._gae_stubs)
        import app

    @classmethod
    def tearDownClass(cls):
        cls.testbed.deactivate()

    @staticmethod
    def login(email, admin=False, user_id=None):
        from os import environ as env
        env['USER_EMAIL'] = email
        env['USER_ID'] = user_id if user_id is not None else ''
        env['USER_IS_ADMIN'] = str(int(admin))
        # env = getattr(self, 'env', {})
        # self.env = env

    @staticmethod
    def logout():
        from os import environ as env
        for name in 'USER_EMAIL', 'USER_ID', 'USER_IS_ADMIN':
            env[name] = ''



class WebAppTestBase(TestBase):
    # Allow to share the setUpClass method among all parallel test classes
    _multiprocess_shared_ = False

    # Allow concurrent run of fixtures
    _multiprocess_can_split_ = False

    @classmethod
    def getApp(cls):
        '''
        Returns list of routes or instance of a WSGIApplication.
        Override this class in your class to test a handler directly.
        '''
        from app import handler
        return handler

    @property
    def app(self):
        import webtest
        app = self.getApp()
        if isinstance(app, (list, tuple)):
            import webapp2
            testapp = webapp2.WSGIApplication(app)
        else:
            testapp = app
        app = webtest.TestApp(testapp)
        return app

    def _app_method(self, method, *args, **kwargs):
        return getattr(self.app, method)(*args, **kwargs)

    def __getattr__(self, name, default=DEFAULT):
        if name in ('get', 'post', 'put', 'delete', 'post_json', 'put_json'):
            return getattr(self.app, name)
        elif name in self.__dict__:
            return self.__dict__[name]
        elif default is not DEFAULT:
            return default
        else:
            raise AttributeError("%s.%s has no attribute %r." % (self.__module__, self.__class__.__name__, name))

import random
import string
from datetime import date, datetime, timedelta
from pprint import pprint
from google.appengine.ext import ndb
class ModelInstanceGenerator(object):

    def __init__(self, model, date_range=(-216000, 216000), string_length=30, text_length=500):
        'date_range ... date range in seconds'
        self.model = model
        self.date_range = date_range
        self.string_length = string_length
        self.text_length = text_length
        self.string_chars = unicode(string.printable) + u'áčďěéíľňóöüúůřšťýžÁČĎĚÉÍĽŇÓÖÜÚŮŘŠŤÝŽ'

    def _gen_StringProperty(self, prop, max_length=None):
        if max_length is None:
            max_length = self.string_length
        length = random.randint(1, max_length)
        return u''.join([random.choice(self.string_chars) for x in xrange(length)])

    def _gen_TextProperty(self, prop):
        return self._gen_StringProperty(prop, max_length=self.text_length)

    def _gen_JsonProperty(self, prop):
        if prop._json_type:
            return prop._json_type()
        else:
            return None

    def _gen_BooleanProperty(self, prop):
        return bool(random.randint(0,1))

    @staticmethod
    def _gen_IntegerProperty(prop):
        return random.randint(0, 9999999)

    def _gen_DateProperty(self, prop):
        return date.today() + timedelta(random.randint(-self.date_range[0] / 3600, self.date_range[1] / 3600))

    def _gen_DateTimeProperty(self, prop):
        return datetime.now() + timedelta(0, random.randint(-self.date_range[0], self.date_range[1]))

    def _gen_LocalStructuredProperty(self, prop):
        return ModelInstanceGenerator(prop._modelclass, date_range = self.date_range).generate()

    @property
    def properties(self):
        return self.model._properties

    def __call__(self, *args, **kwargs):
        return self.generate(*args, **kwargs)

    def generate(self, values=None):
        if values is None:
            values = {}
        for prop_name, prop_type in self.properties.items():
            if isinstance(prop_type, ndb.ComputedProperty):
                continue
            if prop_name not in values:
                if prop_type._choices:
                    genval = lambda prop_type: random.choice(list(prop_type._choices))
                else:
                    genval = lambda prop_type: getattr(self, '_gen_%s' % prop_type.__class__.__name__)(prop_type)
                if prop_type._repeated:
                    values[prop_name] = [genval(prop_type) for n in xrange(random.randint(1, 3))]
                else:
                    values[prop_name] = genval(prop_type)
        try:
            return self.model(**values)
        except Exception:
            pprint(values)
            raise

