# coding=utf-8
from __future__ import absolute_import, unicode_literals

from json import dumps
from functools import wraps

from flask import Response


def jsonify(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        return Response(dumps(func(*args, **kwargs)),
                        mimetype='application/json')
    return wrapped
