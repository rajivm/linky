# coding=utf-8
from __future__ import absolute_import, unicode_literals, print_function


class KeyAlreadyExistsError(StandardError):
        pass


class MemoryDataStore(object):
    __data = {}

    def get(self, key):
        return self.__data.get(key)

    def put(self, key, value, replace=False):
        if not replace and self.get(key) is not None:
            raise KeyAlreadyExistsError(key)
        self.__data[key] = value
