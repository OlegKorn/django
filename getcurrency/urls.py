from django.urls import path
from .views import get_currency


urlpatterns = [
  #path('', get_currency),
  path('', get_currency, name='currency'),
]