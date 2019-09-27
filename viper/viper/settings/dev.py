from .base import *  # noqa

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ho*6)u84ekf-j%6a(z&3msc6#ac8+mxcd4!b))fieve*75%xxb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '0.0.0.0',
    '127.0.0.1',
    'localhost',
]


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'viper',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '0.0.0.0',
        'PORT': '5432',
    }
}


# Caching
# https://docs.djangoproject.com/en/2.2/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://0.0.0.0:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        'KEY_PREFIX': 'viper_rd_cache',
    }
}
CACHE_TTL = 60 * 15  # 15 mins

# Cache Usage Guide:
# https://docs.djangoproject.com/en/2.2/topics/cache/#the-per-view-cache


# Celery integration settings

# Use redis as broker. Note that the DB used should be different from the
# the one the CACHE is using.
CELERY_BROKER_URL = 'amqp://@0.0.0.0:5672'


# LOGGING CONFIGURATION
# https://docs.djangoproject.com/en/dev/topics/logging/
LOGGING['handlers']['file']['level'] = 'DEBUG'

LOGGING['loggers']['django.request']['handlers'] += ['console', 'file']
LOGGING['loggers']['django.request']['level'] = 'DEBUG'

LOGGING['loggers']['default']['handlers'] += ['console']
LOGGING['loggers']['default']['level'] = 'DEBUG'
