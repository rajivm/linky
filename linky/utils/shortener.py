# coding=utf-8
from __future__ import absolute_import, unicode_literals, print_function

from linky.utils.datastore import KeyAlreadyExistsError
import shortuuid
from urlparse import urlparse


class InvalidUrlError(StandardError):
    pass


class Shortener(object):
    def __init__(self, datastore):
        self.datastore = datastore

    @staticmethod
    def __validate_url(url):
        parsed = urlparse(url)
        if parsed.scheme not in ('http, https'):
            return False
        return bool(parsed.netloc)

    def shorten(self, url):
        if not self.__validate_url(url):
            raise InvalidUrlError(url)

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
