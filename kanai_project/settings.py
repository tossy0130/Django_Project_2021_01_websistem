"""
Django settings for kanai_project project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
kanai_projechttps://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9v&!otxb+%*9mszgozg4w^myw)9m*!%b%i3iwn9%*ly2uf*7c='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['13.115.228.94']

BASE_DIR = Path(__file__).resolve().parent.parent
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'widget_tweaks',
    'django_summernote',
    'accounts.apps.AccountsConfig',
    'kanai_app.apps.KanaiAppConfig',
    'calendar_app.apps.CalendarAppConfig',
    'scraping_app.apps.ScrapingAppConfig',
	'kanban.apps.KanbanConfig',
]

### 0524 追加
# AUTH_USER_MODEL='kanai_app.User' 
# AUTH_USER_MODEL = "accounts.CustomUser"
#AUTH_USER_MODEL='kanai_app.CustomUser' 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kanai_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
	 # 今追加したディレクトリを追加
        'DIRS': [os.path.join(BASE_DIR, 'templates')], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                 ############################ templates の中で MEDIA_URL を使えるようにする
                'django.template.context_processors.media', # これを追加する
            ],
        },
    },
]

WSGI_APPLICATION = 'kanai_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
         'ENGINE':'django.db.backends.postgresql_psycopg2',
         'NAME': 'db_tossy_01',
         'USER': 'tossy01',
	 'PASSWORD':'pass',
         'HOST': 'localhost',
         'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

#### 追記
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# STATIC_ROOT = os.path.join(BASE_DIR,'static') # 追加
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] # 追加

########## ログイン、　ログアウト設定
LOGIN_URL = 'kanai_app:login'
LOGIN_REDIRECT_URL = 'kanai_app:kanri_top' # ログイン後　
LOGOUT_REDIRECT_URL = 'accounts:logout'


########## media 画像ファイル設定
MEDIA_ROOT = BASE_DIR / Path('media')
#MEDIA_ROOT = BASE_DIR
MEDIA_URL = '/media/'

########### メディア　画像設定
#MEDIA_ROOT = os.path.join(BASE_DIR,'media') # 追加
#MEDIA_URL = '/media/' # 追加  

SUMMERNOTE_THEME = 'bs4'
X_FRAME_OPTIONS = "SAMEORIGIN"


PROJECT_NAME = os.path.basename(BASE_DIR)
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] 

#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

IMAGE_ROOT = os.path.join(BASE_DIR, 'images')
IMAGE_URL = '/images/'

""" サマーノートの設定 """
SUMMERNOTE_CONFIG = {
    'iframe': True,
    'summernote': {
        'width': '480px',
        'height': '280px',
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'italic', 'clear', ]],
            ['color', ['forecolor', 'backcolor', ]],
            ['misc', ['picture', 'fullscreen', 'codeview', 'print', 'help', ]],
        ],
    },
    'js': (
        '/static/summernote-ext-print.js',
    ),
    'js_for_inplace': (
        '/static/summernote-ext-print.js',
    ),
    'css': (
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.40.0/theme/base16-dark.min.css',
    ),
    'css_for_inplace': (
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.40.0/theme/base16-dark.min.css',
    ),
    'codemirror': {
        'theme': 'base16-dark',
        'mode': 'htmlmixed',
        'lineNumbers': 'true',
    },
    'lazy': False,
}


