routes
======

Url routing to views is realized using `webapp2 routes <http://webapp-improved.appspot.com/guide/routing.html>`__ included in Google Appengine.

The generated project is set to allow include routes recursively. Gap provides special route ``include`` for this purpose.

example:

    src/routes.py:

    .. code:: python
    
        from gap.utils.routes import include
        
        routes = (
            # other routes
            include('/somepath', 'path.to.your.module'),
        )
    
    path/to/your/module.py:
    
    .. code:: python
    
        routes = (
            ('/somepath', 'path.to.your.views.someview'),
            ('/someotherpath', 'path.to.your.views.otherview'),
        )
        
    This way url request to ``/somepath/someotherpath`` will be routed to ``otherview`` in ``path/to/your/views.py``. 

``include`` tries to be inteligent and resolve module path string to real module. If the module / package contains ``routes`` variable, it is used as the list of routes to be included. Otherwise, the path is assumed to be routes list.
You can provide real list or module by as well:

    .. code:: python
    
    from path.to.your import module
    
    routes = (
        # other routes
        include('/soumepath', module.routes),
    )

See `src/routes.py <../gap/templates/src/routes.py>`__ for example of use.
