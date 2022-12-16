from .base import *

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = True

ALLOWED_HOSTS = ["*"]

if os.environ["DATABASE_TYPE"] == "postgresql":
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
    
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
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

STATIC_URL = 'static/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "media/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]