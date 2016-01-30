# Django app to verify the error of DropboxOAuth2Flow().start()

## Setup

1. Install Python 3 and set up virtualenv if you like
1. Install required libraries

        pip install -r requirements.txt

1. Set up environment variables

        touch .env
        vim .env

    Have DROPBOX_CLIENT_ID, DROPBOX_CLIENT_SECRET in the file

1. Set up Django

        ./manage.py migrate

1. Run server

        ./manage.py runserver 5000

1. Access http://localhost:5000/

## Example error

```
Internal Server Error: /
Traceback (most recent call last):
  File "/Users/takeshi/.virtualenvs/djdropbox/lib/python3.5/site-packages/django/core/handlers/base.py", line 235, in get_response
    response = middleware_method(request, response)
  File "/Users/takeshi/.virtualenvs/djdropbox/lib/python3.5/site-packages/django/contrib/sessions/middleware.py", line 50, in process_response
    request.session.save()
  File "/Users/takeshi/.virtualenvs/djdropbox/lib/python3.5/site-packages/django/contrib/sessions/backends/db.py", line 80, in save
    return self.create()
  File "/Users/takeshi/.virtualenvs/djdropbox/lib/python3.5/site-packages/django/contrib/sessions/backends/db.py", line 53, in create
    self.save(must_create=True)
  File "/Users/takeshi/.virtualenvs/djdropbox/lib/python3.5/site-packages/django/contrib/sessions/backends/db.py", line 82, in save
    obj = self.create_model_instance(data)
  File "/Users/takeshi/.virtualenvs/djdropbox/lib/python3.5/site-packages/django/contrib/sessions/backends/db.py", line 68, in create_model_instance
    session_data=self.encode(data),
  File "/Users/takeshi/.virtualenvs/djdropbox/lib/python3.5/site-packages/django/contrib/sessions/backends/base.py", line 88, in encode
    serialized = self.serializer().dumps(session_dict)
  File "/Users/takeshi/.virtualenvs/djdropbox/lib/python3.5/site-packages/django/core/signing.py", line 95, in dumps
    return json.dumps(obj, separators=(',', ':')).encode('latin-1')
  File "/Users/takeshi/.pyenv/versions/3.5.1/lib/python3.5/json/__init__.py", line 237, in dumps
    **kw).encode(obj)
  File "/Users/takeshi/.pyenv/versions/3.5.1/lib/python3.5/json/encoder.py", line 199, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "/Users/takeshi/.pyenv/versions/3.5.1/lib/python3.5/json/encoder.py", line 257, in iterencode
    return _iterencode(o, 0)
  File "/Users/takeshi/.pyenv/versions/3.5.1/lib/python3.5/json/encoder.py", line 180, in default
    raise TypeError(repr(o) + " is not JSON serializable")
TypeError: b'e0wTucORJujkLUnxdxfbWw==' is not JSON serializable
```
