from django.urls import path
from .views import user_log

urlpatterns = [
	path('', user_log, name='login'),
]
