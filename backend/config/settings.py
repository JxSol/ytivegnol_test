import os
from datetime import timedelta
from pathlib import Path

# -------------------------- ADMIN CONFIGURATION ------------------------------
# Django Admin URL.
ADMIN_URL = 'admin/'
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [("""James Nightingale""", 'jxsol.js@gmail.com')]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# -----------------------------------------------------------------------------

#

# -------------------------- PATH CONFIGURATION -------------------------------
# Absolute filesystem path to the Django project directory:
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
# Absolute filesystem path to the directory with applications:
APPS_DIR = BASE_DIR / 'applications'
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]
# -----------------------------------------------------------------------------

#

# -------------------------- GENERAL CONFIGURATION ----------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    default='Cbs0Onr3ARxmK9m2q88OIUytD7qV3TxYtRhky6Z5ijipc7KzxM412V5fx4AtHj5O',
)
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'
# https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'UTC'
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# -----------------------------------------------------------------------------

#

# --------------------------- APPS CONFIGURATION ------------------------------
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    # https://www.django-rest-framework.org/
    'rest_framework',
    'rest_framework.authtoken',
    # https://djoser.readthedocs.io
    'djoser',
    # https://github.com/adamchainz/django-cors-headers
    'corsheaders',
    # https://drf-spectacular.readthedocs.io
    'drf_spectacular',
]

LOCAL_APPS = [
    'applications.users',
]

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# -----------------------------------------------------------------------------

#

# ------------------------- MIDDLEWARE CONFIGURATION --------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# -----------------------------------------------------------------------------

#

# ---------------------------- URLS CONFIGURATION -----------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = 'config.urls'
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'
# -----------------------------------------------------------------------------

#

# -------------------------- TEMPLATES CONFIGURATION --------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# -----------------------------------------------------------------------------

#

# -------------------------- DATABASES CONFIGURATION --------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}
# https://docs.djangoproject.com/en/dev/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# -----------------------------------------------------------------------------

#

# ---------------------------- AUTH CONFIGURATION -----------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = 'users.User'
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# -----------------------------------------------------------------------------

#

# --------------------------- STATIC CONFIGURATION ----------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'
# https://docs.djangoproject.com/en/dev/ref/settings/#staticfiles-dirs
STATICFILES_DIRS = [os.path.join(APPS_DIR, 'static')]
# -----------------------------------------------------------------------------

#

# --------------------------- MEDIA CONFIGURATION -----------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = os.path.join(APPS_DIR, 'media')
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
# -----------------------------------------------------------------------------

#

# ------------------------- EMAIL CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5

# if os.getenv('EMAIL_HOST'):
#     EMAIL_HOST = os.getenv('EMAIL_HOST')
#     EMAIL_PORT = os.getenv('EMAIL_PORT')
#     EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
#     EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
#     EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
#     DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'jxsol.test@gmail.com'
EMAIL_HOST_PASSWORD = 'ilxafyndrgipguwk'
EMAIL_USE_TLS = 'True'
DEFAULT_FROM_EMAIL = 'jxsol.test@gmail.com'
# ------------------------- END EMAIL CONFIGURATION

#

# ------------------- DJANGO REST FRAMEWORK CONFIGURATION ---------------------
# https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# https://github.com/adamchainz/django-cors-headers#cors_urls_regex-str--patternstr
CORS_URLS_REGEX = r'^/api/.*$'

# https://drf-spectacular.readthedocs.io/en/latest/settings.html#settings
SPECTACULAR_SETTINGS = {
    'TITLE': 'Longevity InTime API',
    'DESCRIPTION': 'Documentation of API endpoints of Longevite InTime',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {
        'user': 'applications.users.api.serializers.UserSerializer',
        'current_user': 'applications.users.api.serializers.UserSerializer',
        'token_create': 'applications.users.api.serializers.OTPTokenCreateSerializer',
    },
}
# -----------------------------------------------------------------------------
