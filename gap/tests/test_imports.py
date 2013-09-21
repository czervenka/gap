from gap.utils.test_base import TestBase

from gap.utils.imports import import_class


class TestUtils(TestBase):

    def test_import_class_from_instance(self):
        """ import_class - importing class type from usage """
        timedelta_class = import_class('datetime.timedelta')
        from datetime import timedelta
        self.assertEqual(type(timedelta()), timedelta_class)
        self.assertEqual(type(timedelta()), import_class(timedelta))
