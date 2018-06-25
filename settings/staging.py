from base import *
import dj_database_url


DEBUG = False

# DATABASES = {
#   'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

# Paypal environment variables
PAYPAL_NOTIFY_URL = 'https://discover-thailand.herokuapp.com/'
PAYPAL_RECEIVER_EMAIL = 'discoverthailandbusiness.sandbox@yahoo.com'

SITE_URL = 'https://discover-thailand.herokuapp.com'
ALLOWED_HOSTS.append('discover-thailand.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}