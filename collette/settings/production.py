from collette.settings import *

# Parse database configuration from $DATABASE_URL
import dj_database_url

DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['agile-sierra-7809.herokuapp.com']

if not DEBUG:
    AWS_ACCESS_KEY_ID = 'AKIAIH533NYC56Y3KVKQ'
    AWS_STORAGE_BUCKET_NAME = 'www.collette.co.uk'
    AWS_SECRET_ACCESS_KEY = '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'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATIC_URL = "https://s3-eu-west-1.amazonaws.com/%s" % AWS_STORAGE_BUCKET_NAME


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
        }
    }
}