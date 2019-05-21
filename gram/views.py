from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import User,Profile,Image
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required.

@login_required(login_url='/accounts/login/')
def article(request, profile_id):
def index(request):
    return render(request, 'index.html')

def search_results(request):
    return render(request, 'search_results.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = SignUpRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('signup')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {"gram":gram,"letterForm":form})


