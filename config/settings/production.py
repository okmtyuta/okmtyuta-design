import os

import dotenv

from .base import *

dotenv.load_dotenv()

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]
ALLOWED_HOSTS.extend(os.environ["ALLOWED_HOSTS"].split(","))
CSRF_TRUSTED_ORIGINS = [os.environ["CSRF_TRUSTED_ORIGINS"]]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ["POSTGRES_DB"], 
        'USER': os.environ["POSTGRES_USER"],  
        'PASSWORD': os.environ["POSTGRES_PASSWORD"],  
        'HOST': 'database', 
        'PORT': os.environ["POSTGRES_PORT"], 
    }
}

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


STATIC_URL = 'static/'
STATIC_ROOT = '/home/okmtyuta/.okmtyuta/nginx/public/static'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/okmtyuta/.okmtyuta/nginx/public/media'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]