from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import User,Profile,Image
from .email import send_welcome_email
from .forms import PostImage ,EditProfile
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def profile(request):
    profile_pic=Profile.objects.filter(user=request.user)
    stories=Image.objects.filter(user=request.user)

    
    return render(request, 'profile.html',{'profile':profile_pic,'stories':stories})
@login_required(login_url='/accounts/login/')
def index(request):
    all_images=Image.objects.all()
    return render(request, 'index.html',{"images":all_images})

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

@login_required(login_url='/accounts/login/')
def new_image(request):
    if request.method=='POST':
        form=PostImage(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.user=request.user
            
            image.save()
        return redirect("index")

    else:
        form=PostImage()
    return render(request,"upload.html",{'form':form})

def edit_profile(request):
    if request.method=='POST':
        form=EditProfile(request.POST,request.FILES)
        if form.is_valid():
            edit=form.save(commit=False)
            edit.user=request.user
            edit.save()
        return redirect("profile")
    else:
        form=EditProfile()
    return render(request,'edit.html',{'form':form})


