Testing
==


Introduction, purpose
--
To run tests first install requirements by running bin/gip install -r tests/requirements.gip

Run all tests from anywere by calling tests/run_tests.py

Use test_myapp.py as template to start testing quickly.

If you plan to add setup.py to your app, you can enable `setup.py test` command
by adding

    setup(
        ...
        test_loader='tests.run_tests:TestLoader',
    )

Nose
--
http://nose.readthedocs.org/en/latest/
http://pythontesting.net/framework/nose/nose-introduction/

GAE simulation for unittests
--
https://developers.google.com/appengine/docs/python/tools/localunittesting#Python_Writing_Datastore_and_memcache_tests


Good practice
--
Meaningful test method name and description
KISS - keep all tests short and simple (only few lines)

Inheriting from TestBase brings plenty of useful self.assert* methods
(assertEqual, assertIsNotNone, assertRaises, assertTrue...).

Inherit from gap.utils.test_base.TestBase to get class ready for GAE tests
(with active testbed).

Inherit from gap.utils.tests.WebAppTestBase to start testing views directly.
