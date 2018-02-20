"""
week4solution/resume/admin.py
Feb 19, 2018
"""
from django.contrib import admin
from .models import Experience, Education, Resume

# Register your models here.
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Resume)
