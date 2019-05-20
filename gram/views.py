# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Image
from .forms import NewsLetterForm




def index(request):
     if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            HttpResponseRedirect('index.html')
    else:
        form = NewsLetterForm()
    return render(request, 'index.html', {"gram":gram,"letterForm":form})
  
def search_results(request):
  if 'profile' in request.GET["profile"]:
    search_term = request.GET.get("profile")
    searched_images = Image.search_by_image_profile(search_term)
    message = f"{search_term}"

    return render(request,'index.html',{"message":message,"images": searched_images})


  else:
    message = "You haven't searched for any term"
    return render(request, 'index.html', {"message":message})


def hope.html(request):
  if request.method == 'POST':
    form = NewsLetterForm(request.POST)
    if form.is_valid():
      print('valid')

  else:
    form = NewsLetterForm()
    return render(request, 'index.html', {"gram":gram,"letterForm":form})