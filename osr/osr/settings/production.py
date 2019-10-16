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
SECRET_KEY = os.getenv('SECRET_KEY', '')

DEBUG = True

ALLOWED_HOSTS = [
    os.getenv('SITE_DOMAIN', ''),
]

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
        'ENGINE': os.getenv('DB_ENGINE', ''),
        'NAME': os.getenv('DB_NAME', ''),
        'USER': os.getenv('DB_USER', ''),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', ''),
    }
}


# Cache
# https://docs.djangoproject.com/en/2.1/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': '',
        'LOCATION': '',
    }
}
