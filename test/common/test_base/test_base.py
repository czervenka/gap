# -*- coding: utf-8 -*-
from unittest import TestCase

from google.appengine.ext import testbed


class TestBase(TestCase):

    # Allow to share the setUpClass method among all parallel test classes
    _multiprocess_shared_ = True

    # Allow concurrent run of fixtures
    _multiprocess_can_split_ = True

    @classmethod
    def setUpClass(cls):
        # Begin with testbed instance
        cls.testbed = testbed.Testbed()

        # Activate the testbed environment, this will prepare the service stubs
        cls.testbed.activate()

        # Select all the needed service stubs
        cls.testbed.init_datastore_v3_stub(datastore_file='tmp/datastore.sqlite', use_sqlite=True)
        cls.testbed.init_memcache_stub()

    @classmethod
    def tearDownClass(cls):
        cls.testbed.deactivate()
