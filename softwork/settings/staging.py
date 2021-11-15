from ._base import *

DEBUG = False


# Heroku settings
if os.getcwd() == '/app':
    import dj_database_url
    DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost')
}
# Honor the 'X-Forwarded-Proto' header for request.is_secure().
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Allow all host headers.
ALLOWED_HOSTS = ['*']
# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)