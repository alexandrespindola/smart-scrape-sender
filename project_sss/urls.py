from django.contrib import admin
from django.urls import include, path
from app import views as app_views
from app_sender import views as sender_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_views.index, name='index'),
    path('sender/', include('app_sender.urls')),
]