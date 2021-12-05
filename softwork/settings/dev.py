from ._base import *

DEBUG = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'authme.User'

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend'
]

# we set these parameters to use the email as the User identifier in our authme app:
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

# Also, let’s configure a signup with email verification just for now:
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# to activate the email account after the user clicks on the link received in the email.
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email'
        ],
        
        'AUTH_PARAMS': {
            'access_types': 'online',
        }
    }
}



LOGIN_URL = 'http://127.0.0.1:8000/api/v1/users/login/'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'



# REST_AUTH_REGISTER_SERIALIZERS = {
#     'REGISTER_SERIALIZER': 'softwork.apps.authme.serializers.UserSerializer', 
# }

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'softwork.apps.authme.serializers.UserDetailSerializer'
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
}

REST_USE_JWT = True
JWT_AUTH_COOKIE = "softwork-auth"





