from django.shortcuts import render

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
