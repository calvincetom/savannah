"""
Django settings for savannah project.
"""
from pathlib import Path
from dotenv import load_dotenv

# load .env file
load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "SECRET_KEY"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


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
]

ROOT_URLCONF = "savannah.urls"


# Replace with your domain if you have one.
SITE_URL = "http://localhost:8000"

# AFRICASTALKING API CONF
AFRICASTALKING_USERNAME = "sandbox"
AFRICASTALKING_API_KEY = (
    "atsk_20828f8a69664ad1e18f5fbd543e4b6e867523fc51855ef5a98606b4ba562b4f9aae004f"
)


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
        'NAME': "savannah",
        'USER': "admin",
        'PASSWORD': 'Konza12345',
        'HOST': 'localhost',
        'PORT': 5432
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

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Login and logout redirect url
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/api/v1/"
LOGOUT_REDIRECT_URL = "/"

# Add 'mozilla_django_oidc' authentication backend
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",  # Default Django auth
    "mozilla_django_oidc.auth.OIDCAuthenticationBackend",
)

# OIDC OKTA CONFIG
AUTH0_CLIENT_ID='3WejaIcVvmmGaRmTuqsLnEA835SlhMPS'
AUTH0_CLIENT_SECRET='85eRhu74pvhkUgTzqgxHRRC1VbcLjs52AtRyHncosw_NnuR2uSxUfO4nr99DbPfV'
AUTH0_DOMAIN='dev-77rk2zmat13ucvt2.uk.auth0.com'

# OIDC OKTA CONFIG
OKTA_DOMAIN = 'dev-77rk2zmat13ucvt2.uk.auth0.com'
OIDC_RP_CLIENT_ID = '3WejaIcVvmmGaRmTuqsLnEA835SlhMPS'
OIDC_RP_CLIENT_SECRET = '85eRhu74pvhkUgTzqgxHRRC1VbcLjs52AtRyHncosw_NnuR2uSxUfO4nr99DbPfV'
OIDC_OP_AUTHORIZATION_ENDPOINT = 'https://dev-77rk2zmat13ucvt2.uk.auth0.com/authorize'
OIDC_OP_TOKEN_ENDPOINT = 'https://dev-77rk2zmat13ucvt2.uk.auth0.com/oauth/token'
OIDC_OP_USER_ENDPOINT = 'https://dev-77rk2zmat13ucvt2.uk.auth0.com/userinfo'
OIDC_OP_JWKS_ENDPOINT = f'https://{AUTH0_DOMAIN}/.well-known/jwks.json'
OIDC_OP_LOGOUT_ENDPOINT = 'https://dev-77rk2zmat13ucvt2.uk.auth0.com/v2/logout'

# OIDC Scopes
OIDC_RP_SCOPES = "openid profile email"
OIDC_RP_SIGN_ALGO = "RS256"
