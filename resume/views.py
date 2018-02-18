"""
portfolioplus/resume/views.py for the resume app in portfolioplus
Tiffany
02/10/2018
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
