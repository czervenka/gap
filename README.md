# GAP
Google App Engine is excellent technology but there is a gap.

## If you are missing
* use of pip with Google App Engine,
* cooperation of appengine and virtualenv,
* single python way to add a path to sys.paths,
* Angular.js support out-of-the-box

then this bare-bone could be at least an inspiration for you.

## How to use it (Python part)
* Clone or download the project
* `pip install appengine` or download and install [Appengine SDK](https://developers.google.com/appengine/downloads) 
* Create a virtualenv for you project
* Add your dependencies to `requirements.pip`
* Instal requirements using `bin/gip` same way as you are used to do it with pip
* Start hacking your application under package `src/app`
* You can use any lib you have installed using gip in you code (dev_server, shell as well as after uploading to server).

## How to use it (Angular.js part)
* Install [npm](https://npmjs.org/)
* `npm install -g grunt-cli` - installs [grunt](http://gruntjs.com/) commandline
* `npm install -g bower` - installs [bower](http://bower.io/)
* `npm install` - initializes local grunt
* `bower install` - downloads javascript libraries defined in `bower.json`
* `grunt` - compiles `*.coffee` to `*.js`
* alternatively, `grunt watch` starts watching `src/static/coffee` for changes
* `bin/run` starts dev app server
* navigate to [http://localhost:8080](http://localhost:8080) and enjoy!

Any ideas, thoughts, fixes (specially corrections of my english :) are welcome!

## Disclaimer
Of course ...
This code is published in hope that someone will find it useful but it is provided as-is and I can take **no responsibility** for improper as well as proper
use.