GAP
===

Google App Engine is excelent technology but there is a gap.

If you are missing

-  use of pip with Google App Engine,
-  cooperation of appengine and virtualenv,
-  posibility to add any module to your python path,

then this barebone could be at least an inspiration for you.

How to use (fill) the gap?
--------------------------

-  Install `Google Appengine
   SDK <https://developers.google.com/appengine/downloads>`__
-  Create a virtualenv for you project (not necessary but recomended)
-  pip install gap
-  Go to directory of your new GAE project.
-  gap start-project
-  Add your dependencies to requirements.gip (format of pip
   `requirements
   file <http://www.pip-installer.org/en/latest/cookbook.html>`__)
-  Install any packages using bin/gip same way as you are used to do it
   with pip.
-  To create a new module in your application run gap start-app
-  Keep your code inside src/app.
-  You can use any lib you have installed using gip in your project (in
   dev\_server, shell as well as on appengine server).

See `Gap wiki page <https://github.com/czervenka/gap/wiki>`__ for more
informations.

Any ideas, thoughts, fixes (specially corrections of my english :) are
welcome!

Disclaimer
----------

Of course ... This code is published in hope that someone will find it
usefull but it is provided as-is and I can take no responsibilty for
improper as well as proper use.
