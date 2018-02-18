"""
portfolioplus/resume/urls.py for the resume app in portfolioplus
Tiffany
02/10/2018
"""

from django.urls import path

from . import views

app_name = 'resume'
urlpatterns = [
    path('', views.home, name='resume'),
]