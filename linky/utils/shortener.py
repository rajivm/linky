# coding=utf-8
from __future__ import absolute_import, unicode_literals, print_function

from linky.utils.datastore import KeyAlreadyExistsError
import shortuuid


class Shortener(object):
    def __init__(self, datastore):
        self.datastore = datastore

    def shorten(self, url):
        while True:
            try:
                key = shortuuid.uuid()[:7]
                self.datastore.put(key, url)
                break
            except KeyAlreadyExistsError:
                pass
        return key

    def lookup(self, key):
        return self.datastore.get(key)
