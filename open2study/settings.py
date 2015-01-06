import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = '9*vxwa9!*noptv-8pvqty4i5$z09it@c65+tm-#!cyk%l@n09d'

# If DEBUG is set to False then apache/nginx should serve the static files
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crawlers',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'open2study.urls'

WSGI_APPLICATION = 'open2study.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = 'media'

STATIC_ROOT = 'staticfiles'

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'static/html'),
)

# Static asset configuration for Heroku
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/css'),
    os.path.join(BASE_DIR, 'static/js'),
)
