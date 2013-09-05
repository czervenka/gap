from datetime import timedelta
from test_base import TestBase

from utils.imports import import_class


class TestUtils(TestBase):

    def test_import_class_from_string_path(self):
        delta_two_hours = timedelta(hours=2)
        assert import_class('datetime.timedelta') == type(delta_two_hours)

    def test_import_class_from_usage(self):
        delta_two_hours = timedelta(hours=2)
        assert import_class(timedelta) == type(delta_two_hours)
