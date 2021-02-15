from django.shortcuts import render
from .models import Movie

def film_view(request):
    post = Movie.objects.all()
    context = {
        'posts': post
    }
    return render(request, "film/film-header.html",context)