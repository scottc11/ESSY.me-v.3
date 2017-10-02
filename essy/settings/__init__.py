import os

if os.getenv('GAE_INSTANCE'):
    from .production import *
else:
    from .development import *
