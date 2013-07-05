GAP
==

Google App Engine is excelent technology but there is a gap.

If you are missing

* use of pip with Google App Engine,
* cooperation of appengine and virtualenv,
* single python way to add a path to sys.paths,

then this barebone could be at least an inspiration for you.

How to use it.
--

* Clone or download the project somewhere
* Pip install appengine or download and install Appengine SDK  from
  https://developers.google.com/appengine/downloads
* Creatte an virtualenv for you project
* Add your dependencies to requirements.pip
* Instal requirements using bin/gip same way as you are used to do it with pip
* Start building your application under package src/app
* You can use any lib you have installed using gip in you code (dev_server,
  shell as well as after uploading to server).

Any ideas, thoughts, fixes (specially corrections of my english :) are welcome!


Disclaimer
--
Of course ...
This code is published in hope that someone will find it usefull but it is
provided as-is and I can take no responsibilty for improper as well as proper
use.
