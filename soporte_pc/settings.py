"""
Django settings for soporte_pc project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from decouple import config
import os

# archivos estaticos
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's-vem((20&$14$^0bc6kt+w_@q38$6*7a=x5__hx$u-)&dw^kk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['localhost', '198.211.96.163',
                 'www.soptecpc.com', 'soptecpc.com']
# ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['soptecpc.herokuapp.com',
#                  'soptecpc.herokuapp.com/categoria/views/', '*']

# Para mensajes alertas
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.categoria',
    'apps.usuario',
    'apps.producto',
    'apps.marca',
    'apps.cliente',
    'apps.pedido',
    'apps.datoscuenta',
    'apps.contactanos',
    'apps.quienessomos',
    'apps.comprobante',

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

ROOT_URLCONF = 'soporte_pc.urls'
LOGIN_REDIRECT_URL = '/'

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

WSGI_APPLICATION = 'soporte_pc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# Local

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'soptecpc_bd',
            'USER': 'postgres',
            'PASSWORD': 'yaz',
            'HOST': 'localhost',
            'PORT': 5432,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'soptecbd',
            'USER': 'soptec_admin',
            'PASSWORD': 'alexander19970',
            'HOST': 'localhost',
            'PORT': '',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


password_token = 'computacionyservicio123'

EMAIL_HOST = 'smtp.googlemail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'soptecsoporteonline@gmail.com'
EMAIL_HOST_PASSWORD = password_token
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

LOGIN_URL = "Inicio"

cloudinary.config(
    cloud_name="dndunnh1v",
    api_key="668282533837722",
    api_secret="2LY2dd9FanConC9_k2jbvMwQTmI"
)
