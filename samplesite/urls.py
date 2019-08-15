from django.contrib import admin
from django.urls import path, include
from bboard.views import index

from getcurrency.views import get_currency #app "getcurrency"


urlpatterns = [
    path('', index),
    path('bboard/', include('bboard.urls')),
    path('admin/', admin.site.urls),

    #app "getcurrency"
    path('currency/', include('getcurrency.urls')),
]
