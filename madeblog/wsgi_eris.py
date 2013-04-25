__author__ = 'mad'

import site
site.addsitedir('/home/made/virtualenv/madeblog/lib/python2.6/site-packages')

import os
import sys

sys.path.append('/home/made/www_madeblog')
sys.path.append('/home/made/www_madeblog/blog')

os.environ['DJANGO_SETTINGS_MODULE'] = 'madeblog.settings' #'madeblog.settings_eris'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()