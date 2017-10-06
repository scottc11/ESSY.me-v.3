
import os
import dj_database_url
from .base import *

print('settings: production ')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'PORT': '5432',
    }
}

DATABASES['default']['HOST'] = '/cloudsql/essy-178102:us-central1:essy-db'


STATIC_URL = 'https://storage.googleapis.com/{}/static/'.format(os.environ['CLOUD_STORAGE_BUCKET'])
