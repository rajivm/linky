# coding=utf-8
from __future__ import absolute_import, unicode_literals, print_function

from flask import Flask
from flask import Response
from flask import request
from flask import redirect
from linky.utils.jsonify import jsonify
from linky.utils.shortener import Shortener
from linky.utils.shortener import InvalidUrlError
from linky.utils.datastore import MemoryDataStore

app = Flask(__name__)
shortener = Shortener(MemoryDataStore())


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')


@app.route('/create.json', methods=['POST'])
@jsonify
def create():
    url = request.values.get('url')
    try:
        return Response({'short_url': request.url_root + shortener.shorten(url)})
    except InvalidUrlError:
        return Response({'errors': {'url': 'is invalid'}}, status=400)


@app.route('/<key>.json')
@jsonify
def access_json(key):
    url = shortener.lookup(key)
    if url is None:
        return Response({"error": "link not found"}, status=404)
    return Response({"url": url})


@app.route('/<key>')
def access(key):
    url = shortener.lookup(key)
    if url is None:
        return "link not found", 404
    return redirect(url, 302)


if __name__ == '__main__':
    app.run(debug=True)
