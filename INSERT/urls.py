from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from API import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls))
]
