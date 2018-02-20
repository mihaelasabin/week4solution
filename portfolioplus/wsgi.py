"""
week4solution/portfolioplus/wsgi.py
February 19, 2018
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolioplus.settings")

application = get_wsgi_application()
