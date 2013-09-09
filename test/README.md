Testing
==


Introduction, purpose
--


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


Inheriting from TestBase brings plenty of useful self.assert* methods (assertEqual, assertIsNotNone, assertRaises, assertTrue...)
