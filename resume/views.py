"""
week4solution/resume/views.py
February 19 2018
"""

from django.shortcuts import render
from .models import Resume

# Create your views here.
def home(request):
    """
    Returns the resume app resume template.
    """
    my_resume = Resume.objects.first()
    context = {'my_resume': my_resume}
    return render(request, 'resume/resume.html', context)
