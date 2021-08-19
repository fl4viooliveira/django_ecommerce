from pathlib import Path
from typing import (List, Dict, Tuple, Any)

from environ import Env

env = Env()

BASE_DIR: Path = Path(__file__).resolve().parent.parent
SECRET_KEY: str = env.str('SECRET_KEY', 'default-secret-key')
DEBUG: bool = False
ALLOWED_HOSTS: List[str] = ['www.domain.com', ]
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ROOT_URLCONF: str = 'ecom.urls'
WSGI_APPLICATION: str = 'ecom.wsgi.application'
SITE_ID: int = 1
LOGIN_REDIRECT_URL: str = '/'

# Installed applications
# region
DJANGO_APPS: List[str] = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

REQUIREMENTS_APPS: List[str] = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
]

PROJECT_APPS: List[str] = [
    'cart',
    'core',
    'staff',
]
INSTALLED_APPS = [
    *DJANGO_APPS,
    *REQUIREMENTS_APPS,
    *PROJECT_APPS,
]
# endregion


DEFAULT_FROM_EMAIL = env.str('DEFAULT_FROM_EMAIL', '')
NOTIFY_EMAIL: str = env('NOTIFY_EMAIL', '')

# Middleware
# region
MIDDLEWARE: List[str] = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# endregion

# Templates
# region
TEMPLATES: List[Dict[str, Any]] = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates'],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}, ]
# endregion

# Database
# region
DATABASES: Dict[str, Dict[str, Any]] = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('DATABASE_NAME', 'django_ecommerce'),
        'USER': env.str('DATABASE_USER', 'postgres'),
        'PASSWORD': env.str('DATABASE_PASSWORD', '12345'),
        'HOST': env.str('DATABASE_HOST', 'localhost'),
        'PORT': env.str('DATABASE_PORT', '5432'),
    }
}
# endregion


# Authentication
# region
PASSWORD_HASHES: List[str] = [
    'myproject.hashers.MyPBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

AUTH_PASSWORD_VALIDATORS: List[Dict[str, str]] = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

AUTHENTICATION_BACKENDS: Tuple[str, ...] = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_AUTHENTICATION_METHOD: str = 'email'
ACCOUNT_EMAIL_REQUIRED: bool = True
ACCOUNT_USERNAME_REQUIRED: bool = False
ACCOUNT_EMAIL_VERIFICATION: str = 'mandatory'
# endregion

# Crispy
# region
CRISPY_TEMPLATE_PACK: str = 'bootstrap4'
# endregion

# Language and Timezone
# region
LANGUAGE_CODE: str = 'en-us'
TIME_ZONE: str = 'UTC'
USE_I18N: bool = True
USE_L10N: bool = True
USE_TZ: bool = True
# endregion

# Static and Media
# region
STATIC_URL: str = '/static/'
MEDIA_URL: str = '/media/'

STATICFILES_DIRS: Tuple[Path, ...] = (
    BASE_DIR / 'static',
)

STATIC_ROOT: Path = BASE_DIR / 'static_root'
MEDIA_ROOT: Path = BASE_DIR / 'media_root'
# endregion

# Payment
# region
PAYPAL_CLIENT_ID: str = env.str('PAYPAL_LIVE_CLIENT_ID', '')
PAYPAL_SECRET_KEY: str = env.str('PAYPAL_LIVE_SECRET_KEY', '')

STRIPE_PUBLIC_KEY: str = env.str('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY: str = env.str('STRIPE_SECRET_KEY', '')
STRIPE_WEBHOOK_SECRET: str = env.str('STRIPE_WEBHOOK_SECRET', '')
# endregion

# Session
# region
SESSION_COOKIE_SECURE: bool = True
# endregion

# Secure
# region
SECURE_BROWSER_XSS_FILTER: bool = True
SECURE_CONTENT_TYPE_NOSNIFF: bool = True
SECURE_HSTS_INCLUDE_SUBDOMAINS: bool = True
SECURE_HSTS_SECONDS: int = 31536000  # 365 days = 1 year
SECURE_REDIRECT_EXEMPT: List[str] = []
SECURE_SSL_REDIRECT: bool = True
SECURE_PROXY_SSL_HEADER: Tuple[Tuple[str, str], ...] = (
    ('HTTP_X_FORWARDED_PROTO', 'https'),
)
# endregion
