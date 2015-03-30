"""
Django settings for divided_kingdom project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join, dirname
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


ADMINS = (
    ("Edward Emanuel", "edward.emanuel@gmail.com"),)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!&a8yje^#a3bhl&u_)$l94=9qr3e20y_3@4)#(5zq=f#hzc=2b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

# Application definition

PROJECT_ROOT = dirname(__file__)

TEMPLATE_DIRS = (
    join(PROJECT_ROOT, "templates"),)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "django.contrib.formtools",
    "django.contrib.sites",
    "django.contrib.admindocs",
    "django.contrib.webdesign",

    'south',
    'django_extensions',
    'registration',
    'bootstrap3',
    'annoying',

    'divided_kingdom.apps.core',
    'divided_kingdom.apps.site',
    'divided_kingdom.apps.authentication',
    'divided_kingdom.apps.player',
    'divided_kingdom.apps.registration',
    'divided_kingdom.apps.game',
    'divided_kingdom.apps.item',
    'divided_kingdom.apps.location',
    'divided_kingdom.apps.mob',
    'divided_kingdom.apps.npc',

    'divided_kingdom.apps.phase',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'divided_kingdom.urls'

WSGI_APPLICATION = 'divided_kingdom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'divided_kingdom.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


ACCOUNT_ACTIVATION_DAYS = 7

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = join(PROJECT_ROOT, "public", "static")

STATIC_URL = '/static/'


# Additional locations of static files
STATICFILES_DIRS = (
    join(PROJECT_ROOT, "static"),)

FIXTURE_DIRS = (
    join(PROJECT_ROOT, "fixtures"),
    join(PROJECT_ROOT, "fixtures", "seed"),)


# Sendgrid email settings
#DEFAULT_FROM_EMAIL = "info@dividedkingdom.com"
#EMAIL_HOST = "smtp.sendgrid.net"
#EMAIL_PORT = 587
#EMAIL_HOST_USER = "ej2"
#EMAIL_HOST_PASSWORD = "x9jaher0"
#EMAIL_SUBJECT_PREFIX = "[DividedKingdom]"
#EMAIL_USE_TLS = True
#SERVER_EMAIL = 'system@dividedkingdom.com'

# Sendgrid email settings
DEFAULT_FROM_EMAIL = "SideKick <info@sidecarsinc.com>"
EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_PORT = 587
EMAIL_HOST_USER = "sidecars"
EMAIL_HOST_PASSWORD = "y72mzXgbHYRGry"
EMAIL_SUBJECT_PREFIX = "[Divided Kingdom]"
EMAIL_USE_TLS = True
SERVER_EMAIL = 'system@sidecarsinc.com'
