from django.contrib import admin
from django.urls import path, include
from bboard.views import index, by_rubric


urlpatterns = [
    path('', index),
    path('bboard/', index),
    path('bboard/<int:rubric_id>/', by_rubric),
    path('admin/', admin.site.urls)
]
