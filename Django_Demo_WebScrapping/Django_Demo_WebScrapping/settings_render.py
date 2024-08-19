# from .base import *
from .settings import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['django-demo-webscrapping.onrender.com']

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

IS_LOCAL = False
