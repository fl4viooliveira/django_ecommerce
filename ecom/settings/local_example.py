from .main import *

ALLOWED_HOSTS: List[str] = ['*', ]
EMAIL_BACKEND: str = 'django.core.mail.backends.console.EmailBackend'

# Database
# region
DATABASES: Dict[str, Dict[str, Any]] = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# endregion


# Payment
# region
PAYPAL_CLIENT_ID: str = env.str('PAYPAL_SANDBOX_CLIENT_ID', '')
PAYPAL_SECRET_KEY: str = env.str('PAYPAL_SANDBOX_SECRET_KEY', '')

# endregion

# Session
# region
SESSION_COOKIE_SECURE: bool = False

# endregion
