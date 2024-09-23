"""
Django settings for savannah project.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# load .env file
load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "mozilla_django_oidc",  # Load after auth
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third party libraries
    "rest_framework",
    "orders",
    "phonenumber_field",
    'widget_tweaks' #tailwind css tweaks
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "savannah.urls"


# Replace with your domain if you have one.
SITE_URL = "http://localhost:8000"

# AFRICASTALKING API CONF
AFRICASTALKING_USERNAME = os.environ.get("AFRICASTALKING_USERNAME")
AFRICASTALKING_API_KEY = os.environ.get("AFRICASTALKING_API_KEY")


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "savannah.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('NAME'),
        'USER': os.environ.get('USER'),
        'PASSWORD': os.environ.get('PASSWORD'),
        'HOST': os.environ.get('HOST'),  # Use 'localhost' as a default
        'PORT': 5432  # Use '5432' as a default
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Staocalhosttic files (CSS, JavaScript, Images)
STATIC_URL = "static/"
# Define where collected static files will be stored
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# static file storage
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Login and logout redirect url
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/api/v1/"
LOGOUT_REDIRECT_URL = "/accounts/login/"

# Add 'mozilla_django_oidc' authentication backend
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",  # Default Django auth
    "mozilla_django_oidc.auth.OIDCAuthenticationBackend",
)

# OIDC Auth0 CONFIG
AUTH0_CLIENT_ID = os.environ.get('AUTH0_CLIENT_ID', 'default_client_id')
AUTH0_CLIENT_SECRET = os.environ.get('AUTH0_CLIENT_SECRET', 'default_client_secret')
AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN', 'default_domain')

# OIDC OKTA CONFIG (use the same Auth0 values if applicable)
OKTA_DOMAIN = os.environ.get('OKTA_DOMAIN', AUTH0_DOMAIN)
OIDC_RP_CLIENT_ID = os.environ.get('OIDC_RP_CLIENT_ID', AUTH0_CLIENT_ID)
OIDC_RP_CLIENT_SECRET = os.environ.get('OIDC_RP_CLIENT_SECRET', AUTH0_CLIENT_SECRET)

OIDC_OP_AUTHORIZATION_ENDPOINT = f'https://{AUTH0_DOMAIN}/authorize'
OIDC_OP_TOKEN_ENDPOINT = f'https://{AUTH0_DOMAIN}/oauth/token'
OIDC_OP_USER_ENDPOINT = f'https://{AUTH0_DOMAIN}/userinfo'
OIDC_OP_JWKS_ENDPOINT = f'https://{AUTH0_DOMAIN}/.well-known/jwks.json'
OIDC_OP_LOGOUT_ENDPOINT = f'https://{AUTH0_DOMAIN}/v2/logout'

# OIDC Scopes
OIDC_RP_SCOPES =  'openid profile email'
OIDC_RP_SIGN_ALGO = 'RS256'
