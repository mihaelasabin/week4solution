"""
week4solution/portfolioplus/views.py
February 19, 2018
"""

from django.shortcuts import render

def home(request):
	context = {}
	return render(request, 'home.html', context)


def resume(request):
	context = {}
	return render(request, 'resume.html', context)


def portfolio(request):
	context = {}
	return render(request, 'portfolio.html', context)


def contact(request):
	context = {}
	return render(request, 'contact.html', context)
