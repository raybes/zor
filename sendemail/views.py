# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.shortcuts import render

# Create your views here.

# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            user_email = form.cleaned_data['user_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, user_email, ['admin@zor.me'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact_form.html", {'form': form})

def successView(request):
    return HttpResponse('Your data has entered a void. Success! Please wait for a response, patiently.')