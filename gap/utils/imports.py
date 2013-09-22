#!/usr/bin/env python2
# Copyright 2007 Robin Gottfried <google@kebet.cz>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# @author Robin Gottfried <google@kebet.cz>
# part of gap project (https://github.com/czervenka/gap)

__author__ = 'Robin Gottfried <google@kebet.cz>'

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
