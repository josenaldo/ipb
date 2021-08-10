"""
Django settings for ipb project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import django_heroku
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# TODO: Colocar a secret em outro formato, mais seguro.
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eiq_ia&*t81^@lqn3pg+9%@9+a7++f&o=^u$g0o9vpc*$&@ytd'

# SECURITY WARNING: don't run with debug turned on in production!
# TODO: Configurar o DEBUG dinamicamente, em produção
DEBUG = os.environ.get('DEBUG', False)

ALLOWED_HOSTS = [
    '0.0.0.0',
    'localhost',
    '127.0.0.1',
    'invoca-piroto-backend.herokuapp.com',
    'josenaldo.github.io',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #PLUGINS
    'rest_framework',
    'fullurl',
    #CUSTOM APPS
    'namelist.apps.NamelistConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ipb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'ipb.wsgi.application'

# Messages
# https://docs.djangoproject.com/en/3.2/ref/contrib/messages/

from django.contrib.messages import constants as messages
from django.contrib.messages import constants as message_constants

MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

MESSAGE_LEVEL = message_constants.DEBUG

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {}
DATABASES['default'] = dj_database_url.config(default='postgres://postgres:postgres@localhost/ipb')

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

# REST Configuration
# https://github.com/encode/django-rest-framework

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Redirect to home URL after login
# (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/autenticacao/login/'

# Isso registra todos os emails enviados ao console (para que você 
# possa copiar o link de redefinição de senha do console).
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Configure Django App for Heroku.
django_heroku.settings(locals())
