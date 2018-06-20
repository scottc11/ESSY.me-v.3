import os
import ast
import json
from .base import *

print('settings: production ')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# create a json file to hold google application credentials then
# set envronment variable pointing to that file.
with open('google-app-credentials.json', 'w') as outfile:
    creds = ast.literal_eval(os.environ["GOOGLE_CREDS"]) # convert string to dict
    json.dump(creds, outfile, ensure_ascii=False)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.realpath(outfile.name)


DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'PORT': os.environ['DB_PORT'],
        'HOST': os.environ['DATABASE_HOST'],
    }
}


PROJECT_ID = os.environ['GC_PROJECT_ID']
MEDIA_PREFIX = "static/media/"
CLOUD_STORAGE_BUCKET = os.environ['GC_STORAGE_BUCKET']

STATIC_URL = 'https://storage.googleapis.com/{}/static/'.format(CLOUD_STORAGE_BUCKET)

CLOUD_STORAGE_ROOT = "https://storage.googleapis.com/{bucket_name}/".format(
    bucket_name=CLOUD_STORAGE_BUCKET
)

MEDIA_URL = "{gcs_root}{prefix}/".format(
    gcs_root=CLOUD_STORAGE_ROOT,
    prefix=MEDIA_PREFIX,
)
