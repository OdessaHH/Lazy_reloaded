"""
Django settings for lazyreload project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os  # needed to set environment variables like postgres password
from dotenv import load_dotenv
from pathlib import Path
from datetime import timedelta
import environ


env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(str(BASE_DIR / '.env.prod'))
                  

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.get("SECRET_KEY")


DEBUG=True
# add allowed hosts from railway domain
ALLOWED_HOSTS = ["127.0.0.1",]

CSRF_TRUSTED_ORIGINS = []


# Application definition

INSTALLED_APPS = [
    # core Django apps
    "django.contrib.admin",
    "django.contrib.auth", # Core authentication framework and its default models
    "django.contrib.contenttypes", # Django content type system (allows permissions to be associated with models)
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # third party apps
    # third party apps
    "rest_framework",
    "django_extensions",
    "rest_framework.authtoken",
    "drf_yasg",


    # project apps
    "apps.core",
    "apps.users",
    "apps.job_applications",
    "apps.flat_applications",

    # third party apps
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

AUTH_USER_MODEL = "users.LazyUser"

ROOT_URLCONF = "lazyreload.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [BASE_DIR / 'apps/auth/templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "lazyreload.wsgi.application"



# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# Define Rootfolder for media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# # configure postgres database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'lazyapp',
#         'USER': 'postgres',
#         'PASSWORD': POSTGRES_PW,  # as everyone has a different password set this in .env file
#         'HOST': '127.0.0.1',  # host in development stage
#         'PORT': '5432'
#     }
# }

# if os.environ.get("GITHUB_WORKFLOW"):
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': 'lazyapp',
#             'USER': 'postgres',
#             'PASSWORD': 'postgres',
#             'HOST': '127.0.0.1',
#             'PORT': '5432',
#         }
#     }



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = os.path.join(BASE_DIR,"static/")


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Authentication with Rest Framework

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':[

        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    ]
}

# from mentoring
STATIC_ROOT = str(BASE_DIR / 'staticfiles')
STATICFILES_DIRS = (str(BASE_DIR / "static"), )

# connect to database remotely getting the database like with dj database

import dj_database_url

DATABASE_URL = env.str("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.config(default=DATABASE_URL),
}
