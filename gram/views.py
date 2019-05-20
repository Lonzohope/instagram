# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image

# Create your views here.


def index(request):

  return render(request, 'index.html')

def search_results(request):
  if 'profile' in request.GET["profile"]:
    search_term = request.GET.get("profile")
    searched_images = Image.search_by_image_profile(search_term)
    message = f"{search_term}"

    return render(request,'index.html',{"message":message,"images": searched_images})


  else:
    message = "You haven't searched for any term"
    return render(request, 'index.html', {"message":message})