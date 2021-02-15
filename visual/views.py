from django.shortcuts import render
from .models import Visual

def visual(request):
    post = Visual.objects.all()
    context = {
        'posts': post
    }
    return render(request, "visual/visual-header.html",context)