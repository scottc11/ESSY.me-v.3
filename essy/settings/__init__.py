import os

if os.environ.get('IS_HEROKU', None):
    from .production import *
else:
    from .development import *
