from .base import *

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'https://discover-thailand.herokuapp.com/'
PAYPAL_RECEIVER_EMAIL = 'discoverthailandbusiness.sandbox@yahoo.com'
