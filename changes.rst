Version 0.4.9
-------------
- gip
  1. some packages caused gip not to work properly
  2. ``-v`` option shows a lot of debug informations
- minor fixes in documentation
- invalid import in new poject's views.py

Version 0.4.8
-------------
- mainly enhancements in test suite
  1. executable flag on run_test
  2. added base class for testing views
  3. support for rednose in tests (rednose seems not compatible with multiprocess plugin)
  4. Test* classes not imported in utils.__init__ (forced test requirements even when running gap project)
  5. test requirements ignored by gip (not usefull on production)
- fixed link in changelog
- extended Route class which can better handle ending slash

Version 0.4.7
-------------
- documentation (see `doc/index.rst` or on `github <https://github.com/czervenka/gap/blob/master/doc/index.rst>`__)

Version 0.4.3, 0.4.5
--------------------
- fixed missing README.rst in MANIFEST.in (sorry)
- changes added to package description

Version 0.4
-----------

-  tests in project template (application tests)
-  bin/ipython in project runs ipython (if installed) with gae testbed
   stubs
-  new apps have model template file now
-  better template loaders to allow install 3rd party modules
-  default 404 page now shows list of routes
-  gap tests can be run from setup.py test
-  settings can have defaults in config.py (refer to project's
   config.py:DEFAULT\_SETTINGS)

Version 0.3
-----------

-  added some tests
-  added baseTest classes (many thanks to Lukas Lukovsky)
-  added gap.conf.settings (highly cached db stored settings)
-  minor fixes in setup.py

Version 0.2
-----------

Major rewrite to enable installation using pip and project creation a-la
django.

-  first version of setup.py

Version 0.1
-----------

Never released
