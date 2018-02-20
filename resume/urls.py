"""
week4solution/resume/urls.py
February 19, 2018
"""

from django.urls import path

from . import views   # resume/urls.py

app_name = 'resume'
urlpatterns = [
    path('', views.home, name ='resume'),
]