from .base import *


DEBUG = False

try:
    from .local import *
except ImportError:
    pass


import os

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = ['*']

if os.environ.get('OPENSHIFT_DATABASE_TYPE') == 'PostgreSQL':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('OPENSHIFT_POSTGRESQL_DB_NAME'),
            'USER': os.environ.get('OPENSHIFT_POSTGRESQL_DB_USERNAME'),
            'PASSWORD': os.environ.get('OPENSHIFT_POSTGRESQL_DB_PASSWORD'),
            'HOST': os.environ.get('OPENSHIFT_POSTGRESQL_DB_HOST'),
            'PORT': os.environ.get('OPENSHIFT_POSTGRESQL_DB_PORT')
        }
    }
elif os.environ.get('OPENSHIFT_DATABASE_TYPE') == 'MySQL':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('OPENSHIFT_MYSQL_DB_NAME'),
            'USER': os.environ.get('OPENSHIFT_MYSQL_DB_USERNAME'),
            'PASSWORD': os.environ.get('OPENSHIFT_MYSQL_DB_PASSWORD'),
            'HOST': os.environ.get('OPENSHIFT_MYSQL_DB_HOST'),
            'PORT': os.environ.get('OPENSHIFT_MYSQL_DB_PORT')
        }
    }
