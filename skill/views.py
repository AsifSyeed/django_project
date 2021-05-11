from django.shortcuts import render

def home(request):

	title = 'Hello everyone this is nemes1s'
	descript = 'Developer/ Music Composer/ Gamer'


	return render(request, 'index.html', {'title': title, 'description': descript})

def about(request):

	title = 'About Me'
	descript = 'I am a developer working with a mindset to grow my skills. Besides, I work as music composer/ guitarist/ bassist. I play games in my pastimes.'

	context = {
		'title': title,
		'aboutDescription': descript,
	}
	return render(request, 'about.html', context)

def contact(request):
	return render(request, 'contact.html')