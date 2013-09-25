settings
========

Gap supports `settings <../gap/conf.py>`__ stored in GAE storage. Settings are
heavily cached and changes are propagated across threads and frontends (both
using memcached).

Example:
    .. code:: python
    
        >>> from gap.conf import settings
        >>> settings['version']
        u'0'
    
    An attempt to read unset value will lead to KeyError
    
    .. code:: python

        >>> settings['my_setting']
        KeyError: 'Key "my_setting" not found.'
    
    Writing to unset key will raise KeyError as well
    
    .. code:: python
    
        >>> settings['my_settings'] = 1
        KeyError: "Settings property 'my_settings' is not defined yet."
                  "Please use add_setting method to add new property."
        
    You have to register new settings using add_setting
    
    .. code:: python
    
        >>> settings.add_settings('my_setting') = 1
        >>> settings['my_settings']
        1
        
    You can also unregister any setting
    
    .. code:: python

        >>> settings.del_setting('my_setting')
        >>> settings['my_setting']
        KeyError('Key "my_setting" not found.')


The `settings object <../gap/conf.py>`__ is optimized for reading not for
writing (which is most common way of using settings).

Reading is cheap and lazy. The actual data are being read from storage when
first value is read on frontend and the data are stored in package until
frontend shutdown or reload triggered by modification on other fronted.

When a value is modified, settings writes it immediately to storage and
propagates the change to the other fronteds (using memcache).

Be careful, there is now locking mechanism. Your application logic must supply
a mechanism how to prevent concurrent writes to settings from parallel
threads/frontends (this can change in future).
