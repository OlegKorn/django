from django.urls import path
from .views import get_search


urlpatterns = [
    path('search/', get_search),
]

