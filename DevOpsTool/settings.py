"""
Django settings for DevOpsTool project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path
from environs import Env

import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = "/data/logs/devopstool/"
Path(LOG_DIR).mkdir(parents=True, exist_ok=True)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DJANGO_DEBUG")

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'debug_toolbar',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',

    # Local
    'accounts',
    'pages',
    'environments',
    'applications',
    'deployments',
]

MIDDLEWARE = [
    'deployments.performance.PerformanceMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'DevOpsTool.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
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

WSGI_APPLICATION = 'DevOpsTool.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DJANGO_DB_NAME"),
        'USER': env("DJANGO_DB_USER"),
        'PASSWORD': env("DJANGO_DB_PASSWORD"),
        'HOST': env("DJANGO_DB_HOST"),
        'PORT': env("DJANGO_DB_PORT")
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))

AUTH_USER_MODEL = 'accounts.CustomUser'

AUTHENTICATION_BACKENDS = (
    "django_auth_ldap.backend.LDAPBackend",
    'django.contrib.auth.backends.ModelBackend',
)

# Baseline configuration.
AUTH_LDAP_SERVER_URI = env("DJANGO_AUTH_LDAP_SERVER_URI")

AUTH_LDAP_BIND_DN = env("DJANGO_AUTH_LDAP_BIND_DN")
AUTH_LDAP_BIND_PASSWORD = env("DJANGO_AUTH_LDAP_BIND_PASSWORD")

AUTH_LDAP_USER_SEARCH_BASE_DN = env("DJANGO_AUTH_LDAP_USER_SEARCH_BASE_DN")
AUTH_LDAP_USER_SEARCH_FILTER = env("DJANGO_AUTH_LDAP_USER_SEARCH_FILTER")

AUTH_LDAP_USER_SEARCH = LDAPSearch(
    AUTH_LDAP_USER_SEARCH_BASE_DN,
    ldap.SCOPE_SUBTREE,
    AUTH_LDAP_USER_SEARCH_FILTER,
)

AUTH_LDAP_GROUP_SEARCH_BASE_DN = env("DJANGO_AUTH_LDAP_GROUP_SEARCH_BASE_DN")
AUTH_LDAP_GROUP_SEARCH_FILTER = env("DJANGO_AUTH_LDAP_GROUP_SEARCH_FILTER")
# Set up the basic group parameters.
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    AUTH_LDAP_GROUP_SEARCH_BASE_DN,
    ldap.SCOPE_SUBTREE,
    AUTH_LDAP_GROUP_SEARCH_FILTER,
)

AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr='cn')

AUTH_LDAP_MIRROR_GROUPS = True

# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    'first_name': 'givenName',
    'last_name': 'sn',
    'email': 'mail',
}

AUTH_LDAP_ALWAYS_UPDATE_USER = True

# Use LDAP group membership to calculate group permissions.
AUTH_LDAP_FIND_GROUP_PERMS = True

# Cache distinguished names and group memberships for an hour to minimize
# LDAP traffic.
AUTH_LDAP_CACHE_TIMEOUT = 3600

INTERNAL_IPS = ['127.0.0.1']

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(name)-12s %(lineno)d %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'auth': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'simple',
            'filename': os.path.join(LOG_DIR, 'devopstool.auth.log'),
            'maxBytes': 1024 * 1024,  # 1M
            'backupCount': 5,
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'simple',
            'filename': os.path.join(LOG_DIR, 'devopstool.admin.log'),
            'maxBytes': 1024 * 1024,  # 1M
            'backupCount': 5,
        },
        'performance': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'simple',
            'filename': os.path.join(LOG_DIR, 'devopstool.performance.log'),
        },
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': env('DJANGO_LOG_LEVEL'),
            'propagate': True,
        },
        'django_auth_ldap': {
            'level': env('DJANGO_LOG_LEVEL'),
            'handlers': ['auth'],
            'propagate': False,
        },
        "deployments.performance": {
            "handlers": ["performance"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:9000",
    "http://localhost:8081",
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

CELERY_BROKER_URL = 'redis://' + env('DJANGP_CELERY_REDIS_HOST') + ':' + env('DJANGP_CELERY_REDIS_PORT') + '/' + env('DJANGP_CELERY_BROKER_DB')
CELERY_RESULT_BACKEND = 'redis://' + env('DJANGP_CELERY_REDIS_HOST') + ':' + env('DJANGP_CELERY_REDIS_PORT') + '/' + env('DJANGP_CELERY_RESULT_DB')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYD_MAX_TASKS_PER_CHILD = 10
CELERYD_LOG_FILE = os.path.join(LOG_DIR, "celery_work.log")
CELERYBEAT_LOG_FILE = os.path.join(LOG_DIR, "celery_beat.log")
