Testing
=======

Tests can not only save time and help keep project bug-free but tests are often
the the only source of up to date documentation.

Gap uses `nose <http://nose.readthedocs.org/en/latest/testing.html>`__ and
`Google's testbed <https://developers.google.com/appengine/docs/python/tools/localunittesting>`__.

Installing test requirements
----------------------------

Beforu you can use tests, install test requirements with ``bin/gip install tests/requirements.gip``.

Running project tests
---------------------

To run project tests is as easy

.. code:: sh

    > cd tests
    > python run_tests.py

    Always True ... ok

    ------------------------
    Ran 1 test in 0.164s

    OK

and - of cource - you can run just one test by ``python run_tests test_myapp``
(where test_myapp is the module with tests).

There is no need to have dev server running to start tests.

Writing your test
-----------------

The simplest way to write a test is to copy the test_myapp.py empty test and
start adding custom tests for your project.

Gap helps writing tests with two tools

:TestBase: Base class which sets gae services and isolated datastore
:ipython: ``bin/ipython`` live testing environment

Simple example test:

.. code:: python

    from gap.utils import TestBase

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

Because ``gap.conf.settings`` uses datastore to save values and memcached to check for
changes from other instances (see `settings <settings.rst>`__), this test also
shows that gae datastore and memcached services are working in the test
environment. This is main benefit of TestBase class.

bin/ipython
-----------

There are two scenarios when you start writing test.

1. You plan to code a modul or a class and want to have tests first to describe the task.
2. You already have a working piece of code and want to add tests for documentation and testing.

If the second is you case then ipython could help. Just start the interactive
console by calling bin/ipython and start writing the test cases. In the
examples above I just started to play with settings in interactive ipython console:

.. code:: python

    > bin/ipython.py
    Python 2.7.2 (default, Oct 11 2012, 20:14:37)
    In [1]: from gap.conf import settings
    In [2]: settings['somekey'] = 1
    --> 129             raise KeyError("Settings property %r is not defined yet. Please use add_setting method to add new property." % key)
    KeyError: "Settings property 'somekey' is not defined yet. Please use add_setting method to add new property."

    In [3]: settings.add_setting['somekey']
    ----> 1 settings.add_setting['somekey']
    TypeError: 'instancemethod' object is not subscriptable

    In [4]: settings.add_setting('somekey')
    ----> 1 settings.add_setting('somekey')
    TypeError: add_setting() takes exactly 3 arguments (2 given)

    In [5]: settings.add_setting('somekey', 1)
    In [6]: settings['somekey']
    Out[6]: 1

and after trial / error I typed magical ``%history``

.. code:: python

    In [7]: %history
    from gap.conf import settings
    settings['somekey'] = 1
    settings.add_setting['somekey']
    settings.add_setting('somekey')
    settings.add_setting('somekey', 1)
    settings['somekey']
    %history

\.\. and here we are. Just finish the test commands and fill them to the
assertXxxx statements. The bin/ipython script sets up the same environment as
is used in tests. And - what I like - no dev_appserver needs to run to play in
ipython and application data are really changed.
