from django.http import HttpResponse

def home(request):

	html = """ 
	<h1> Home Page </h1>
	<p> Welcome to the home page! </p>
	"""
	return HttpResponse(html)

def contact(request):
	return HttpResponse('Contact Us')

def about(request):
	return HttpResponse('About us')