Extending The Gap
=================

*Gap covers only basic features commonly used in various types of GAE project. To extend the functionality of gap, you can easily create extension packages.*

How to create an extension
--------------------------

Gap is Python and therefor any extension is just a Python package. All third-party packages are installed to src/lib using bin/gip utility.

Common ways to integrate you package to gap

Gap prefers explicit before implicit magic. Better to direct developer to few values in config.py or routes.py than auto-magically set them silently. There is therefor no automatic package installation procedure in gap (not counting gip). Each package should contain a README file describing how to setup the package.

Gap is still written with regard to extension packages:
    
routes:
    Common way to add routes easily is to use gap.utils.routes.include. Your routes can be set to ie. /mypackage/.* by editing `src/route <https://github.com/czervenka/gap/blob/versions/0.4.7/gap/templates/src/routes.py>`__ file:
    
    .. code:: python

        routes = (
            ...
            include('/mypackage', 'lib.mypackage.routes'),
            ...
        )

    Your package should always use `webapp2.uri_for(...) <http://webapp-improved.appspot.com/api/webapp2.html#webapp2.uri_for>`__ method to get uri for your view.
    
settings:
    Package could use gap.conf.settings stored in storrage. The default values can be set by calling setting.add_setting or by adding new keys to config.DEFAULT_SETTINGS of the project (should be mentioned in README).
    
templates:
    Your package template dirs can be included by adding directories to config.TEMPLATE_PATHS of the project.

static files:
    Static files can only be added by modifying src/app.yaml. The recomended way is to add include.yaml to your package and your package to app.yaml (should be mentioned in README)
    
requirements:
    As extension packages are installable using gip (pip wrapper) use Python distutils to specifie any requirements your package needs to install / test / run.
