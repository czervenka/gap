from types import StringTypes

def import_class(class_name):
    """
    imports and returns class by its path

    USAGE:
        myclass = import_class('StringIO.StringIO')
        # or
        from StringIO import StringIO
        myclass = import_class(StringIO)
    """
    if isinstance(class_name, StringTypes):
        from importlib import import_module
        module_name, class_name = class_name.rsplit('.', 1)
        module = import_module(module_name)
        return getattr(module, class_name)
    else:
        return class_name
