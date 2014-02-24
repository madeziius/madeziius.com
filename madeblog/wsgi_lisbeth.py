__author__ = 'made'

import site
site.addsitedir('/var/www/madeblog/env/lib/python2.7/site-packages')

import os
import sys

sys.path.append('/var/www/madeblog')
sys.path.append('/var/www/madeblog/madeblog')
sys.path.append('/var/www/madeblog/blog')

os.environ['DJANGO_SETTINGS_MODULE'] = 'madeblog.settings_lisbeth' #'madeblog.settings_eris'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
