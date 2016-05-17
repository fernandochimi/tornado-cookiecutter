import os
import json

import tornado.ioloop
import tornado.web
import tornado.options

from tornado.options import options
from tornado.options import define

from settings import settings

from apps.urls import urls


class Application(tornado.web.Application):
    settings = {
        'debug': settings.DEBUG,
        'gzip': getattr(settings, 'GZIP', False),
        'cookie_secret': settings.SECRET_KEY,
        'xsrf_cookies': getattr(settings, 'XSRF_COOKIES', False),
        'autoescape': "xhtml_escape",
        'template_path': settings.TEMPLATE_ROOT,
        'static_path': settings.STATIC_ROOT,
        'static_url_prefix': settings.STATIC_URL,
    }

    def __init__(self):
        tornado.web.Application.__init__(self, urls, **self.settings)


def info(attr):
   meta = dict()
   with open(os.path.join(settings.PROJECT_DIR, 'app.json'), 'r') as content:
       meta = json.load(content)

       info = meta.get(attr)
       if info:
           return info
       else:
           raise ValueError('App info missing attribute {0} '.format(attr))


def make_app():
    app = Application()
    return app

if __name__ == '__main__':
    make_app()
