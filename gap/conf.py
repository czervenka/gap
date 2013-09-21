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

"""
Simple database app settings

BASIC USE
---------
    from app_settings import settings
    version = settings['version']  # read settings
    settings['version'] = '1'  # stores settings

INITIALIZATION
--------------
    from gap.conf import settings
    settings['version'] = '1'  # new version is automatically written to db
    settings.add_setting('my_new_setting', 'Initial value')   # adds new setting property to db
    settings.add_setting('my_structured_property', {'title': 'Title'})  # adds new structured property
    settings['my_structured_property'].title
    >> 'Title'
"""
import logging
from uuid import uuid1

from google.appengine.ext import ndb
from google.appengine.api import memcache


class AppSettings(ndb.Expando):

    KEY = 'app_settings'
    _default_indexed = False

    version = ndb.StringProperty(default='0', indexed=False)

    @classmethod
    def get_key(cls):
        return ndb.Key(cls, cls.KEY)

    def put(self, *args, **kwargs):
        self.set_uuid()
        if not self.key:
            self.key = self.get_key()
        # self.key.delete(use_datastore=False)  # flush ndb model cache
        super(self.__class__, self).put(*args, **kwargs)

    @classmethod
    def get_uuid(cls):
        return memcache.get('AppSettings:version')

    @classmethod
    def set_uuid(cls):
        uuid = uuid1()
        memcache.set('AppSettings:version', uuid)


class LazyAppSettings(object):
    """
    Settings row property descriptor used in SettingsDict.
    """

    #@ndb.transactional
    def __get__(self, instance, owner=None):
        uuid = AppSettings.get_uuid()
        if not hasattr(instance, '_cached_settings') or getattr(instance, '_cached_uuid', None) != uuid:
            key = ndb.Key(AppSettings, AppSettings.KEY)
            row = key.get()
            if row is None:
                row = AppSettings(key=key)
                row.put()
            instance._cached_settings = row
            instance._cached_uuid = uuid
            logging.debug('Getting settings')
        return instance._cached_settings


class SettingsDict(object):
    """
    Dictionary which reads settings from database.

    To list all settings simply calll settings.items()
    """

    _data = LazyAppSettings()

    def _set_settings(self, dict_data):
        self._data = dict_data

    def __getitem__(self, key):
        if hasattr(self._data, key):
            value = getattr(self._data, key)
            if isinstance(value, ndb.Expando):
                oldsetter = value.__setattr__
                def new_setter(obj, key, value):
                    oldsetter(key, value)
                    self.save()

                value.__setattribute__ = new_setter
            return value
        else:
            raise KeyError('Key %s not found.' % key)

    # @ndb.transactional
    def __setitem__(self, key, value):
        if not key in self:
            raise KeyError("Settings property %r is not defined yet. Please use add_key method to add new property." % key)
        setattr(self._data, key, value)
        self.save()

    # @ndb.transactional
    def add_setting(self, key, value):
        if key in self:
            raise KeyError("The property %r already exists.")
        setattr(self._data, key, value)
        self.save()

    def save(self):
        self._data.put()

    def reload(self):
        delattr(self, '_cached_uuid')

    def del_setting(self, key):
        delattr(self._data, key)
        self._data.put()

    def __hasitem__(self, key):
        return key in self.keys()

    def __contains__(self, key):
        return hasattr(self._data, key)

    def keys(self):
        return self._data._properties.keys()

    def items(self):
        return [(key, self[key]) for key in self.keys()]

    def values(self):
        return [self[key] for key in self.keys()]

    def __iter__(self):
        for key in self.keys():
            yield key


settings = SettingsDict()
