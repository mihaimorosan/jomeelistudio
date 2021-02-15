from django.shortcuts import render
from .models import AboutMe

def about_me(request):
    post = AboutMe.objects.all()
    context = {
        'posts':post
    }
    return render(request, "about-me/about-me-header.html",context)