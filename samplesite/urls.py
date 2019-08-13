from django.contrib import admin
from django.urls import path, include
from bboard.views import index


urlpatterns = [
    path('', index),
    path('bboard/', index),
    path('admin/', admin.site.urls)
]
