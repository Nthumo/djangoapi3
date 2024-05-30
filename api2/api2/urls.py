from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    re_path(r'^', include('djangoapi2.urls')),
    path('admin/', admin.site.urls),
]
