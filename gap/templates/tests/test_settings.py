from gap.utils.tests import TestBase

class TestMyApplication(TestBase):
    '''Example tests set'''

    def test_settings(self):
        '''settings'''
        key = 'some_nonexisting_key'
        value = 'my value'
        from gap.conf import settings
        self.assertRaises(KeyError, lambda: settings[key])
        settings.add_setting(key, value)
        self.assertEquals(settings[key], value)
