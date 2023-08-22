from .base import *   #LLAMANDO AL ARCHIVO BASE 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []



import os

if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['apiTest'],
            'USER': os.environ['triunfo'],
            'PASSWORD': os.environ['triunfo2023'],
            'HOST': os.environ['databaseaws1.ctpv9egj42p9.sa-east-1.rds.amazonaws.com'],
            'PORT': os.environ['5432'],
        }
    }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'


