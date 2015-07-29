# coding=utf-8
from __future__ import absolute_import, unicode_literals, print_function

from flask import Flask
from flask import request
# from linky.utils import jsonify
from linky.utils.shortener import Shortener
from linky.utils.datastore import MemoryDataStore

app = Flask(__name__)
shortener = Shortener(MemoryDataStore())


@app.route('/s/<key>')
def access(key):
    url = shortener.lookup(key)
    if url is None:
        return "link not found", 404
    return url


@app.route('/create.json', methods=['POST'])
def create():
    url = request.values.get('url')
    return shortener.shorten(url)


if __name__ == '__main__':
    app.run(debug=True)
