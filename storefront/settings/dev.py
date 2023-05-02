import os
import environ
from .base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = []

INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS +=[
    'debug_toolbar',
]

MIDDLEWARE+=[
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER':env('DB_USER'),
        'PASSWORD':env('DB_PASSWORD'),
        'PORT':3306,
    }
}