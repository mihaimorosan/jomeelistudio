from django.contrib import admin
from django.urls import path, include

from . import views
from .views import ProjectListView, ProjectDetailView

urlpatterns = [
    path('', views.photography),
    path('events/', views.events_photography_view),
    path('events/ryerson-events/', views.events_ryerson_events_view),
    path('events/tce/', views.events_tce_view),
    path('creative/', ProjectListView.as_view(), name='project_list'),
    path('creative/<slug:slug>', ProjectDetailView.as_view(), name='project'),
]