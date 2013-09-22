from gap.conf import settings
from gap.utils.test_base import TestBase


class TestSettings(TestBase):
    '''gap.conf.settings'''

    def test_initial_settings_value(self):
        """settings['version'] is not None"""
        self.assertIsNotNone(settings['version'])

    def test_store_settings_value(self):
        """settings returns stored value"""
        settings['version'] = '1'
        self.assertEqual(settings['version'], '1')

    def test_read_not_existing_settings_value(self):
        """settings reading non-existing key raises KeyError"""

        def set_key(key, value):
            settings[key] = value

        self.assertRaises(KeyError, lambda x: x['non_existing_key'], settings)
        self.assertRaises(KeyError, set_key, 'non_existing_key', 1)

    def test_add_setting(self):
        '''settings - new setting can be added and removed'''
        self.assertRaises(KeyError, lambda: settings['new_property'])
        settings.add_setting('new_property', 255)
        self.assertEqual(settings['new_property'], 255)
        settings.del_setting('new_property')
        self.assertRaises(KeyError, lambda: settings['new_property'])

    def test_composed_setting(self):
        '''settings - structured value save settings when changed'''
        settings.add_setting('test', {'a': 1})
        self.assertEqual(settings['test'].a, 1)
        settings['test'].a = 2
        self.assertEqual(settings['test'].a, 2)
        settings.reload()
        self.assertEqual(settings['test'].a, 2)

    def test_default_settings(self):
        '''settings - default values are read from conf'''
        from gap import conf
        self.assertRaises(KeyError, lambda: settings['mytest'])
        conf.DEFAULT_SETTINGS['mytest'] = 'hokus pokus'
        self.assertEqual(settings['mytest'], 'hokus pokus')

    def test_separate_namespace_values(self):
        """ Settings - values in different namespaces are not affecting each other """

        from google.appengine.api import namespace_manager

        namespace_manager.set_namespace('namespace_1')
        settings['version'] = '1'

        namespace_manager.set_namespace('namespace_2')
        settings['version'] = '2'

        namespace_manager.set_namespace('namespace_1')
        self.assertEqual('1', settings['version'])
