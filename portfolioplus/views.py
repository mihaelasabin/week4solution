"""
portfolioplus/views.py for the portfolioplus Python package in week 3 container
Tiffany
02/10/2018
"""

from django.shortcuts import render

def home(request):
	"""
	Takes request of type HttpRequest and calls render() with ustudy.html file and empty context.
	request: has information about current request that triggered this view
	Returns: home page of week 2 portfolio site
	"""
	
	context = {}
	return render(request, 'home.html', context)


def resume(request):
	"""
	Takes request of type HttpRequest and calls render() with ustudy.html file and empty context.
	request: has information about current request that triggered this view
	Returns: resume page of week 2 portfolio site
	"""

	context = {}
	return render(request, 'resume.html', context)


def portfolio(request):
	"""
	Takes request of type HttpRequest and calls render() with ustudy.html file and empty context.
	request: has information about current request that triggered this view
	Returns: portfolio page of week 2 portfolio site
	"""

	context = {}
	return render(request, 'portfolio.html', context)


def contact(request):
	"""
	Takes request of type HttpRequest and calls render() with ustudy.html file and empty context.
	request: has information about current request that triggered this view
	Returns: contact page of week 2 portfolio site
	"""

	context = {}
	return render(request, 'contact.html', context)
