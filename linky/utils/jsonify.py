# coding=utf-8
from __future__ import absolute_import, unicode_literals

from json import dumps
from functools import wraps


def jsonify(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        response = func(*args, **kwargs)
        response.response = dumps(response.response)
        response.content_type = 'application/json'
        return response
    return wrapped
