from django.utils import timezone
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import RyersonEvent, TCEModel, Creative

def photography(request):
    return render(request, "photography/photography-header.html")

def events_photography_view(request):
    return render(request, "photography/events/events-header.html")

def events_ryerson_events_view(request):
    post = RyersonEvent.objects.all()
    context = {
        'posts':post
    }
    return render(request, "photography/events/ryerson-events/ryerson-events-header.html",context)

def events_tce_view(request):
    post = TCEModel.objects.all()
    context = {
        'posts':post
    }
    return render(request, "photography/events/tce/tce-header.html", context)

class ProjectListView(ListView):
    model = Creative
    template_name = "photography/creative/creative-header.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ProjectDetailView(DetailView):
    model = Creative
    template_name = "photography/creative/project/project-header.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context