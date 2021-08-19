from .main import *

ALLOWED_HOSTS: List[str] = ['*', ]
EMAIL_BACKEND: str = 'django.core.mail.backends.console.EmailBackend'

# Payment
# region
PAYPAL_CLIENT_ID: str = env.str('PAYPAL_SANDBOX_CLIENT_ID', '')
PAYPAL_SECRET_KEY: str = env.str('PAYPAL_SANDBOX_SECRET_KEY', '')

# endregion

# Session
# region
SESSION_COOKIE_SECURE: bool = False

# endregion
