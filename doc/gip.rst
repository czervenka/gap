gip
===

Gip is in fact a thin wrapper around standard `Python pip installer <http://www.pip-installer.org>`__. The only difference is, that gip keeps track of installed packages and links / unlinks them to your project's `src/lib <../gap/templates/src/lib>`__ directory.

You need to install project-specific packages in virtualenv for gip to work properly. Any packages installed globally will by ignored.

When deploing your project to Appengine symbolic links are resolved and libraries from src/lib are uploaded to Google's servers. This way you can yous full advantage of pip installer.

I highly recomend to use requirements.gip (which is created by gip during ``gip start-project`` command). Anyone other who needs to work on your project will just setup virtualenv and ``run bin/gip install -r requirements.gip``. See `pip's requirements file format <http://www.pip-installer.org/en/1.0.1/requirement-format.html>`__ for more info.
