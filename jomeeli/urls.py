from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('film/', include('film.urls')),
    path('photography/', include('photography.urls')),
    path('visual/', include('visual.urls')),
    path('about-me/', include('about_me.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)