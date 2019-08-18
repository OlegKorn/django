from django.contrib import admin
from django.urls import path, include
from bboard.views import index
from search.views import get_search


urlpatterns = [
    path('', index),
    path('bboard/', include('bboard.urls')),
    path('admin/', admin.site.urls),

    #app "getcurrency"
    path('currency/', include('getcurrency.urls')),

    #app "search"
    path('search/', get_search),
]
