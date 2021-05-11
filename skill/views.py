from django.shortcuts import render
from .models import skill, ContactInfo

def home(request):

	title = 'Hello everyone this is nemes1s'
	descript = 'Developer/ Music Composer/ Gamer'

	item = skill.objects.all()

	context = {
		'title': title,
		'description': descript,
		'data': item,
	}

	return render(request, 'index.html', context)

def about(request):

	title = 'About Me'
	descript = 'I am a developer working with a mindset to grow my skills. Besides, I work as music composer/ guitarist/ bassist. I play games in my pastimes.'

	context = {
		'title': title,
		'aboutDescription': descript,
	}
	return render(request, 'about.html', context)

def contact(request):

	if  request.method == 'POST':

		name = request.POST.get('name')
		email = request.POST.get('email')
		comment = request.POST.get('comments')

		saveData = ContactInfo()
		saveData.cName = name 
		saveData.cEmail = email
		saveData.cComment = comment

		saveData.save()

	return render(request, 'contact.html')