from .base import *

DEBUG = False

ADMINS = (
    ('Ashish R', 'dev98@cock.li'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': 'educapassword',
    },
}
