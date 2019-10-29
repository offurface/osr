import os
from dotenv import load_dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_ROOT)
PUBLIC_DIR = os.path.join(os.path.dirname(BASE_DIR), 'public')
SITE_NAME = os.path.basename(PROJECT_ROOT)
ENV_PATH = os.path.join(os.path.dirname(BASE_DIR), '.env')

load_dotenv(dotenv_path=ENV_PATH)

# Application definition
DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'widget_tweaks',
    'import_export',

    'apps.account.apps.AccountConfig',
    'apps.registry.apps.RegistryConfig',
]

DEFAULT_MIDDLEWARE = [
    # 'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = '%s.urls' % SITE_NAME

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'ru'
LANGUAGES = (
    ('ru', 'Русский'),
)

# THOUSAND_SEPARATOR = ' '
# USE_THOUSAND_SEPARATOR = True

TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PUBLIC_DIR, 'static')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static', 'dist'),
]


# Media files
# https://docs.djangoproject.com/en/2.1/ref/settings/#media-root
MEDIA_ROOT = os.path.join(PUBLIC_DIR, 'media')
MEDIA_URL = '/media/'


# Login urls
# https://docs.djangoproject.com/en/2.1/ref/settings/#login-url
LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


# Email
# https://docs.djangoproject.com/en/2.1/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', '')
EMAIL_PORT = os.getenv('EMAIL_PORT', '')
EMAIL_HOST_USER = os.getenv('EMAIL_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD', '')
EMAIL_USE_SSL = True
EMAIL_SUBJECT_PREFIX = ''
SERVER_EMAIL = os.getenv('EMAIL_NAME', '')
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_NAME', '')
MANAGERS = [
    ('Manager', os.getenv('EMAIL_MANAGER', '')),
]

#AUTH_USER_MODEL = ''
SITE_ID = 1
