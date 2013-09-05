# -*- coding: utf-8 -*-
from unittest import TestCase

from google.appengine.ext import testbed


class TestBase(TestCase):

    # Allow to share the setUpClass method among all parallel test classes
    _multiprocess_shared_ = True

    # Allow concurrent run of fixtures
    _multiprocess_can_split_ = True

    def setUp(self):
        # Begin with testbed instance
        self.testbed = testbed.Testbed()

        # Activate the testbed environment, this will prepare the service stubs
        self.testbed.activate()

        # Select all the needed service stubs
        self.testbed.init_datastore_v3_stub(datastore_file='tmp/datastore.sqlite', use_sqlite=True)
        self.testbed.init_memcache_stub()

    def tearDown(self):
        self.testbed.deactivate()
