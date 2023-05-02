import os
from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1','localhost']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER':os.environ.get('DB_USER'),
        'PASSWORD':os.environ.get('DB_PASSWORD'),
        'PORT':3306,
    }
}