from django.shortcuts import render,redirect
from .models import Post
from .forms import LoginForm, PostForm, SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group
# from django.contrib.auth.decorators import login_required

# -------------------------------------------------------|
# Home
def home(request):
    post = Post.objects.all()
    return render(request,'blog/home.html',{'posts':post})

# About
def about(request):
    return render(request,'blog/about.html')

# Contact
def contact(request):
    return render(request,'blog/contact.html')

# DashBoard
# @login_required
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request,'blog/dahboard.html',{'posts':posts,'full_name':full_name,'groups':gps})
    else:
        return redirect('/login')

# Signup
def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,'Congratulations !! You have become a author ✔✔👍')
            # user =User.objects.get()
            group= Group.objects.all()
            for i in group:
                print(i)
            # user.groups.add(group)
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
                    return redirect('/dashboard/')
                else:
                    messages.error(request,'username or password is invalid')
        else:
            form = LoginForm()
        return render(request,'blog/login.html',{'form':form})
    else:
        return redirect('/dashboard/')
    
# logout
def user_logout(request):
    logout(request)
    return redirect('/')

# Add a post
def addPost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            print(form)
            if form.is_valid:
                addtitle = form.cleaned_data['title']
                adddesc = form.cleaned_data['desc']
                pst = Post(title = addtitle, desc= adddesc)
                pst.save()
                print(pst)
                form = PostForm()
        else:
            form = PostForm()
        return render(request,'blog/addpost.html',{'form':form})
    else:
        return redirect('/login/')
    
# Update a Post
def updatePost(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST,instance=pi)
            if form.is_valid:
                form.save()
        else:
            pi = Post.objects.get(id=id)
            form = PostForm(instance=pi)
        return render(request,'blog/updatepost.html',{'form':form})
    else:
        return redirect('/login/')
    
# Delete post
def deletePost(request,id):
    if request.user.is_authenticated:
        print(id,type())
        if request.method == "Post":
            pi = Post.objects.get(pk=id)
            print(pi,id)
            pi.delete()
            return redirect('dashboard')
    else:
        return redirect('login')
