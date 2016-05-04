from tornado import web
from tornado.web import URLSpec as url
from library.urls import include

from library.conf import settings

from .core.views import HomeHandler


urls = [
    url(r"/", HomeHandler),
    url(r"/static/(.*)", web.StaticFileHandler, {"path": settings.get('static_path')}),
]

urls += include(r"/healthcheck", "apps.core.urls")
urls += include(r"/customers", "apps.customers.urls")
