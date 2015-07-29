# Linky: Basic Link Shortener

### Warning

This is not production ready software. It is just a proof-of-concept.

### Setup

```
pip install virtualenv
```
In the project's directory:
```
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Now you may access the running url shortening service at http://localhost:5000/

### API

```
POST /create.json
```
This endpoint accepts a query-string or form-body parameter of 'url' and returns a json response:
```
{"short_url": "http://127.0.0.1:5000/zMdVhVw"}
```
If the submitted url is invalid, the service will return a 400 error.


```
GET /{key}.json
```
If .json is appended to a short url, instead of redirecting, it will return a JSON response with the destination URL:
```
{"url": "http://www.example.com"}
```