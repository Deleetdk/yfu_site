"""
WSGI config for yfu_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

sys.path.append('/home/emil/server/yfu/yfu/yfu_site')
sys.path.append('/home/emil/server/yfu/yfu')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yfu_site.settings")

#this makes the admin panel css work
application = Cling(get_wsgi_application())
#application = get_wsgi_application()
