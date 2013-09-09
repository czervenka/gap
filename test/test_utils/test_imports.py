from datetime import timedelta
from common.test_base import TestBase

from utils.imports import import_class


class TestUtils(TestBase):

    def test_import_class_from_string_path(self):
        """ Utils - importing class type from string path """
        delta_two_hours = timedelta(hours=2)
        self.assertEqual(type(delta_two_hours), import_class('datetime.timedelta'))

    def test_import_class_from_usage(self):
        """ Utils - importing class type from usage """
        delta_two_hours = timedelta(hours=2)
        self.assertEqual(type(delta_two_hours), import_class(timedelta))
