
import os
import dj_database_url
from .base import *
from YamJam import yamjam

print('settings: development ')

CFG = yamjam()['essy']

SECRET_KEY = CFG['django_secret_key']

DEBUG = True


DATABASES = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': CFG['local_psql']['database_name'],
        'USER': CFG['local_psql']['user']['name'],
        'PASSWORD': CFG['local_psql']['user']['pass'],
        'PORT': '5432',
        'HOST': '127.0.0.1'
    },
    'heroku': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': CFG['heroku_psql']['database_name'],
        'USER': CFG['heroku_psql']['user']['name'],
        'PASSWORD': CFG['heroku_psql']['user']['pass'],
        'PORT': '5432',
        'HOST': '127.0.0.1'
    }
}

PROJECT_ID = 'essy-178102'
CLOUD_STORAGE_BUCKET = 'essy-dev'
MEDIA_PREFIX = "media/"

CLOUD_STORAGE_ROOT = "https://storage.googleapis.com/{bucket_name}/".format(
    bucket_name=CLOUD_STORAGE_BUCKET
)

MEDIA_URL = "{gcs_root}{prefix}/".format(
    gcs_root=CLOUD_STORAGE_ROOT,
    prefix=MEDIA_PREFIX,
)
