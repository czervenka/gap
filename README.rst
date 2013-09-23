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
- create virtualenv::

    > pip install gap
    > gap start-project <applicationid>
    > cd <applicationid>
    > appcfg update src

Long version
------------

1.   Install
     `Google Appengine SDK <https://developers.google.com/appengine/downloads>`__
2.   Create a virtualenv for you project (not necessary but recommended)
3.   pip install gap
4.   Go to directory of your new GAE project.
5.   gap start-project
6.   Add your dependencies to requirements.gip (format of pip
    `requirements file <http://www.pip-installer.org/en/latest/cookbook.html>`__)
7.   Install any packages using bin/gip same way as you are used to do it
     with pip.
8.   To create a new module in your application run gap start-app
9.   Keep your code inside src/app.
10.  You can use any lib you have installed using gip in your project (in
     dev\_server, shell as well as on appengine server).

See `Gap wiki page <https://github.com/czervenka/gap/wiki>`__ for more
informations.

Any ideas, thoughts, fixes (specially corrections of my English :) are
welcome!

Disclaimer
==========

Of course ... This code is published in hope that someone will find it
useful but it is provided as-is and I can take no responsibility for
improper as well as proper use.
