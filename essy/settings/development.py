
import os
import dj_database_url
from .base import *
from YamJam import yamjam

print('settings: development ')

CFG = yamjam()['essy']

SECRET_KEY = CFG['django_secret_key']

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'test': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': CFG['cloud_sql']['database_name'],
        'USER': CFG['cloud_sql']['user']['name'],
        'PASSWORD': CFG['cloud_sql']['user']['pass'],
        'PORT': '5432',
    }
}


DATABASES['default']['HOST'] = '/cloudsql/essy-178102:us-central1:essy-db'

if os.getenv('GAE_INSTANCE'):
    pass
else:
    DATABASES['default']['HOST'] = '127.0.0.1'



STATIC_URL = '/static/'
