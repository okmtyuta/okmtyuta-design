import os

import dotenv

from .base import *

dotenv.load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["nostalon.jp", "okmtyuta.nostalon.jp", "api.nostalon.jp"]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nostalon', 
        'USER': 'okmtyuta',  
        'PASSWORD': 'h_r*NTS9kiFx',  
        'HOST': '160.16.132.244', 
        'PORT': '3306', 
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = '/home/okmtyuta/.okmtyuta/nginx/public/static'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/okmtyuta/.okmtyuta/nginx/public/media'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]