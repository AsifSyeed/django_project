from django.shortcuts import render

def user_log(request):
	return render(request, './auth/login.html', {})