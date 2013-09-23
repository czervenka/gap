GAP
###

Google App Engine is excellent technology but there is a gap.

If you are missing

-  use of pip with Google App Engine,
-  cooperation of appengine and virtualenv,
-  possibility to add any module to your python path,

then this barebone could be at least an inspiration for you.

How to use (fill) the gap?
==========================

Short version
-------------
create virtualenv
::

    > pip install gap
    > gap start-project <applicationid>
    > cd <applicationid>
    > appcfg update src

Long version
------------

1.   Install
     `Google Appengine SDK <https://developers.google.com/appengine/downloads>`__
2.   Create a `virtualenv <http://www.virtualenv.org/en/latest/>`__ for you project
3.   if necessary ``easy_install pip``
4.   run ``pip install gap``
5.   Go to directory where you want to create your GAE project.
6.   run ``gap start-project <projectname>``  # <projectname> will be used as applicationId
7.   Add your dependencies to requirements.gip (format is the same as pip
     `requirements file <http://www.pip-installer.org/en/latest/cookbook.html>`__) and
     run ``bin/gip install -r requirements.gip``
8.   or install any packages using bin/gip same way as you are used to do it
     with pip.
9.   To create a new module in your application run ``gap start-app <module_name>``
10.  Keep your code inside ``src/app``
     (see ``wiki::Pip support <https://github.com/czervenka/gap/wiki/Pip-support>`` for details).
11.  Libraries installed using gip are accessible in dev_server as well as on GAE servers.

See `Gap wiki page <https://github.com/czervenka/gap/wiki>`__ for more
informations.

Any ideas, thoughts, fixes (specially corrections of my English :) are
welcome!

Disclaimer
==========

Of course ... This code is published in hope that someone will find it
useful but it is provided as-is and I can take no responsibility for
improper as well as proper use.
