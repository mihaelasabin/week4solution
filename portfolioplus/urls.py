"""
week4solution/portfolioplus/urls.py 
February 19, 2018
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resume/', include('resume.urls', namespace='resume')),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('admin/', admin.site.urls),
]
