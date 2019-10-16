import os
from dotenv import load_dotenv
from .common import (
    ENV_PATH,
    PUBLIC_DIR,
    DEFAULT_APPS,
    DEFAULT_MIDDLEWARE,
)

load_dotenv(dotenv_path=ENV_PATH)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rbcbc$y1w==xmpf(s-j$gssej_vogtjdm@-vhezu66h_l0b7uf'

DEBUG = True

INTERNAL_IPS = ['127.0.0.1', ]
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    *DEFAULT_APPS,

]

MIDDLEWARE = [
    *DEFAULT_MIDDLEWARE,

]

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(
            PUBLIC_DIR, 'db.sqlite3'
        ),
        'TEST': {
            'NAME': os.path.join(
                PUBLIC_DIR, 'test_db.sqlite3'
            ),
        },
    },
}
