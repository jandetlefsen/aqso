import os, sys
sys.path.append('/opt/bitnami/apps')
sys.path.append('/opt/bitnami/apps/osqa')
os.environ['DJANGO_SETTINGS_MODULE'] = 'osqa.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
