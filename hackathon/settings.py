"""
Django settings for hackathon kit project.
Dan Borstelmann August 28, 2016

Production settings file to select proper environment variables.
"""

import os
from django.core.exceptions import ImproperlyConfigured
import dj_database_url


def get_env_variable(environment_variable, optional=False):
    """Get the environment variable or return exception"""
    try:
        return os.environ[environment_variable]
    except KeyError:
        if optional:
            return ''
        else:
            error = "environment variable '{ev}' not found.".format(ev=environment_variable)
            raise ImproperlyConfigured(error)

DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = get_env_variable("DJANGO_HACKATHON_KIT_SECRET_KEY")
ALLOWED_HOSTS = [".herokuapp.com"]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'authentication',
    'frontend_views'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware', TODO: fix eventually
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True
ROOT_URLCONF = 'hackathon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "webapp/templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hackathon.wsgi.application'

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'webapp/static'),
)


if 'HACKATHON_KIT_LOCAL_NAME' not in os.environ:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

    DATABASES = {
        'default': dj_database_url.parse(get_env_variable("DATABASE_URL"))
    }
else:
    DATABASES = {
        'default': {
            'HOST': 'localhost',
            'PORT': '5432',
            'NAME': get_env_variable("HACKATHON_KIT_LOCAL_NAME"),
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': get_env_variable("HACKATHON_KIT_LOCAL_USERNAME"),
            'PASSWORD': get_env_variable("HACKATHON_KIT_LOCAL_PASSWORD"),
        },
    }

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
