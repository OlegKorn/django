from django.contrib import admin
from django.urls import path, include
from bboard.views import (
    index,
    get_test #test
)

from getcurrency.views import get_currency #app "getcurrency"


urlpatterns = [
    path('', index),
    path('bboard/', include('bboard.urls')),
    path('admin/', admin.site.urls),
    path('test/', get_test), #test

    #app "getcurrency"
    path('currency/', include('getcurrency.urls')),
]
