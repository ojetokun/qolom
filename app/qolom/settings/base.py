"""
Django settings for qolom project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")


INSTALLED_APPS = [
                        'core',
                        'account',
                        'users.apps.UsersConfig',
                        'business',
                        'rest_framework',

            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'django_cleanup.apps.CleanupConfig',
            'django_filters'

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

WSGI_APPLICATION = 'qolom.wsgi.application'


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

REST_FRAMEWORK = {
        'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
        'DEFAULT_RENDERER_CLASSES': [
            'rest_framework.renderers.JSONRenderer',
    ]

}
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

ROOT_URLCONF = 'qolom.urls'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'account.User'

AUTH_FROM_EMAIL = 'Qolom <auth@qolom.com>'

ORDERING_FEES = 0.02 # 2/100
# CRONJOBS = [
#     ('* * * * *', 'business.cron.job')
# ]

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static',]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

EMAIL_USE_TLS = True
EMAIL_HOST = os.environ.get("SMTP_EMAIL_HOST")
EMAIL_PORT = os.environ.get("SMTP_EMAIL_PORT")
EMAIL_HOST_USER = os.environ.get("SMTP_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("SMTP_EMAIL_PASSWORD")




PASSWORD_RESET_TIMEOUT = 1800

PAYSTACK_WHITELISTED_IPS = [
    '129.205.124.243','52.31.139.75',
    '52.49.173.169','52.214.14.220'
]

PAYSTACK_SECRET_KEY = os.environ.get("PAYSTACK_SECRET_KEY")












