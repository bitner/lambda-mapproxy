# WSGI module for use with Apache mod_wsgi or gunicorn

from mapproxy.wsgiapp import make_wsgi_app
app = make_wsgi_app(r'mapproxy.yaml')
