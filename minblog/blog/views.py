from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm, SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
# Home
def home(request):
    return render(request,'blog/home.html')
# About
def about(request):
    return render(request,'blog/about.html')
# Contact
def contact(request):
    return render(request,'blog/contact.html')
# DashBoard
def dashboard(request):
    return render(request,'blog/dahboard.html')
# Signup
def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations !! You have become a author ✔✔👍')
            form.save()
    else:
        form = SignUpForm()
    return render(request,'blog/signup.html',{'form':form})
# Login 
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request,data= request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate( username = uname,password = upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully')
                    return HttpResponseRedirect('/dashboard/')
                else:
                    messages.error(request,'Invalid Username or Password')
        else:
            form = LoginForm()
        return render(request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')
# logout
def user_logout(request):
    return HttpResponseRedirect('/')
