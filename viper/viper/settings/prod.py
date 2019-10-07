from .base import *  # noqa

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '84dfb51412774dcab2219d05a37a69fb)32=d21d&423$3221dfkkeQQssf?>'

ALLOWED_HOSTS = [
    'viper.local',
    '192.168.56.114',
]


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'viper',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Caching
# https://docs.djangoproject.com/en/2.2/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
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
CELERY_BROKER_URL = 'amqp://@127.0.0.1:5672'
