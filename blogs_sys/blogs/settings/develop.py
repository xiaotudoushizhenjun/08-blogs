#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Author  : xiaotudou
@time: 2019/07/17 8:27
@File    : develop.py 
'''
from .base import *  # NOQA
# 引入base的所有配置


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogs',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
        # 'CONN_MAX_AGE': 5 * 60,
        # 'OPTIONS': {'charset': 'utf8m64'}
    }
}

INSTALLED_APPS += [
    'debug_toolbar',
    # 'pympler',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']


# DEBUG_TOOLBAR_PANELS = [
#     'djdt_flamegraph.FlamegraphPanel',
# ]

# DEBUG_TOOLBAR_CONFIG = {
#     'JQUERY-URL': 'https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js',
# }