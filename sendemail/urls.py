from django.contrib import admin
from django.urls import path

from .views import contactView, successView

urlpatterns = [
	path('message_us/', contactView, name='contact_us'),
	path('confirmation_success/', successView, name='success'),
]