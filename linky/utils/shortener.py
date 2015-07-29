# coding=utf-8
from __future__ import absolute_import, unicode_literals, print_function


class Shortener(object):
    def __init__(self, datastore):
        self.datastore = datastore
        self.next_id = 1

    def shorten(self, url):
        key = unicode(self.next_id)
        self.datastore.put(key, url)
        self.next_id += 1
        return key

    def lookup(self, key):
        return self.datastore.get(key)
