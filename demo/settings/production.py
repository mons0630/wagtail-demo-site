from .base import *


DEBUG = False

try:
    from .local import *
except ImportError:
    pass


import os

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRESQL_DATABASE', 'wagtail'),
        'USER': os.environ.get('POSTGRESQL_USER', 'wagtail'),
        'PASSWORD': os.environ.get('POSTGRESQL_PASSWORD', 'wagtail'),
        'HOST': os.environ.get('POSTGRESQL_HOST', 'wagtaildb'),
        'PORT': os.environ.get('POSTGRESQL_PORT', '5432'),
    }
}
