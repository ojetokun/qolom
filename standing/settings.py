"""
Django settings for standing project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
#from django.urls import reverse_lazy,reverse
from django_hosts.resolvers import reverse_lazy
import os, platform, django_heroku


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-unv$5@-^k3(p_+h=5^zw55+d0x9lb+y&dc!&x1vwo8n(2(@5w'

# SECURITY WARNING: don't run with debug turned on in production!

if platform.system()=='Windows':
    DEBUG = True
else:
    DEBUG = False

if DEBUG:
    ALLOWED_HOSTS = ['172.20.10.3','admin.172.20.10.3','media.172.20.10.3',
                 'media.localhost','admin.localhost','localhost',
		'media.qolom.com','admin.qolom.com','qolom.com','babalawo.herokuapp.com','admin.babalawo.herokuapp.com',
        'media.babalawo.herokuapp.com']
else:
    ALLOWED_HOSTS = ['media.qolom.com','admin.qolom.com','qolom.com']

LOGIN_URL = reverse_lazy('login')


# Application definition

INSTALLED_APPS = [
                        'core',
                        'account',
                        'users.apps.UsersConfig',
                        'business',
                        'paystack.frameworks.django',
                        'rest_framework',

            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'django_cleanup.apps.CleanupConfig',

            'django_crontab',
            'django_hosts',


]

MIDDLEWARE = [
    'django_hosts.middleware.HostsRequestMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django_hosts.middleware.HostsResponseMiddleware',
]

ROOT_URLCONF = 'standing.urls'
ROOT_HOSTCONF = 'standing.hosts'

if DEBUG:
    PARENT_HOST = 'localhost:8000'
else:
    PARENT_HOST = 'qolom.com'
    
DEFAULT_HOST = 'www'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'users.context_processors.special_line',
                'users.context_processors.get_business',
                'users.context_processors.ready_order',
            ],
        },
    },
]

WSGI_APPLICATION = 'standing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
if DEBUG:
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'qolom',
        'USER': 'postgres',
        'PASSWORD': os.getenv("POSTGRES_PASSWORD"),
        'HOST': '127.0.0.1',
        'PORT': '',
        }
    }

else:
     DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'website_database',
        'USER': 'lanre',
        'PASSWORD': 'iscoreng123',
        'HOST': 'localhost',
        'PORT': '',
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
        'TIMEOUT': 60,
        'OPTIONS': {
            'MAX_ENTRIES': 100000, #100,000
            'CULL_FREQUENCY':100,
        }
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

AUTH_USER_MODEL = 'account.User'

AUTH_FROM_EMAIL = 'Qolom <auth@qolom.com>'

CRONJOBS = [
    ('* * * * *', 'business.cron.job')
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static',]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.domain.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'support@qolom.com'
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASSWORD")




PASSWORD_RESET_TIMEOUT = 1800


#PAYSTACK_SCRET_KEY = 'sk_live_ac2b02dea7ded9c765e8603a58538911a3e724b5'
PAYSTACK_SCRET_KEY = 'sk_test_dba3ece03b5a28cc32f000e6eb82ff58e5d690e7'

django_heroku.settings(locals())

















# """
# Django settings for standing project.

# Generated by 'django-admin startproject' using Django 3.1.

# For more information on this file, see
# https://docs.djangoproject.com/en/3.1/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/3.1/ref/settings/
# """

# from pathlib import Path
# from django.urls import reverse_lazy
# import os
# import django_heroku


# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '-unv$5@-^k3(p_+h=5^zw55+d0x9lb+y&dc!&x1vwo8n(2(@5w'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = ['172.20.10.3','localhost','babalawo.herokuapp.com']
# LOGIN_URL = reverse_lazy('login')


# # Application definition

# INSTALLED_APPS = ['account',
#                   'users',
#                   'business',
#                   'paystack.frameworks.django',
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'django_cleanup.apps.CleanupConfig',
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
# ]

# ROOT_URLCONF = 'standing.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'standing.wsgi.application'


# # Database
# # https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'website_database',
#         'USER': 'lanre',
#         'PASSWORD': 'iscoreng123',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }



# # Password validation
# # https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# # Internationalization
# # https://docs.djangoproject.com/en/3.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_L10N = True

# USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.1/howto/static-files/

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / 'static',]
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'

# EEMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'ojetoks@gmail.com'
# EMAIL_HOST_PASSWORD = 'Iscoreng123?'
# EMAIL_PORT = 587


# PASSWORD_RESET_TIMEOUT = 600



# PAYSTACK_SCRET_KEY = 'sk_live_ac2b02dea7ded9c765e8603a58538911a3e724b5'


# django_heroku.settings(locals())
















