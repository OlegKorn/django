from django.urls import path
from .views import get_test


urlpatterns = [
    path('', get_test),
]

