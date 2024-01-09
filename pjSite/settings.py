"""
Django settings for pjSite project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+7jmp3fm-x64)@(amzr=8ir9qi!-*)hsbcsw+m+t32^z=5&2(('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 새로운 앱 생성 관련 항목
    'web_lib',
    'single_pages',
    'board',

    # 게시글 입력 관련 양식 제작을 위한 항목
    'crispy_forms',                 # django에서 양식을 제작하는 데 사용되는 기본 style을 제공하는 외부 라이브러리
    
    # 이하 계정 관리를 위한 항목
    'django.contrib.sites',                     # site 관리
    'allauth',                                  # allauth 앱
    'allauth.account',                          # 계정 관리
    'allauth.socialaccount',                    # 소셜 계정 관리
    'allauth.socialaccount.providers.google',   # 구글 로그인
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pjSite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'pjSite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False                  #>> User Time Zone (기본은 True였는데 프로젝트 진행시 False로 변경함.)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'                             # 정적 파일(css, image 등)을 연결하고자 하는 파일을 담는 기본 경로

MEDIA_URL = '/media/'                               # 파일 업로드 관련해서 폴더 추가 (관련 내용을 사용하기 위해서는 os를 import 해줘야 함.)
MEDIA_ROOT = os.path.join(BASE_DIR, "_media")       # _media 폴더 생성

CRISPY_TEMPLATE_PACK = 'bootstrap4'                 # 'INSTALLED_APPS'에 등록한 'crispy_forms'에 사용하고자 하는 외부 라이브러리 설정.

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',                # 사용자명과 비밀번호를 이용한 인증을 지원
    'allauth.account.auth_backends.AuthenticationBackend',      # 이메일 주소를 이용한 인증 등 추가적인 인증 방식을 지원
]


SITE_ID = 2         # 사이트 아이디 지정

ACCOUNT_EMAIL_REQUIRED = True           # 회원가입시 이메일 필수
ACCOUNT_EMAIL_VERIFICATION = 'none'     # 이메일 인증 필요 없음
LOGIN_REDIRECT_URL = '/board/'          # 로그인 후 이동 페이지