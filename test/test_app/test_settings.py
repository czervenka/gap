from app.settings import settings
from common.test_base import TestBase


class TestSettings(TestBase):

    def test_initial_settings_value(self):
        """ Settings - initial version value is not None """
        self.assertIsNotNone(settings['version'])

    def test_store_settings_value(self):
        """ Settings - stored version value to settings is returned back """
        settings['version'] = '1'
        self.assertEqual('1', settings['version'])

    def test_read_not_existing_settings_value(self):
        """ Settings - reading not existing value fails """
        def read_not_existing_value():
            return settings['not_existing_key']
        self.assertRaises(KeyError, read_not_existing_value)

    def test_separate_namespace_values(self):
        """ Settings - values in different namespaces are not affecting each other """

        from google.appengine.api import namespace_manager

        namespace_manager.set_namespace('namespace_1')
        settings['version'] = '1'

        namespace_manager.set_namespace('namespace_2')
        settings['version'] = '2'

        namespace_manager.set_namespace('namespace_1')
        self.assertEqual('1', settings['version'])
